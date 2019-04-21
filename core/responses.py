import six
from rest_framework.response import Response as rf_Response
from rest_framework.serializers import Serializer

from core.exceptions import ERROR_PHRASES


class Response(rf_Response):

    def __init__(self, data=None, status=None,
                 template_name=None, headers=None,
                 error_code=None, error_message=None,
                 exception=False, content_type=None,
                 biz=True):

        super().__init__(None, status=status)

        if isinstance(data, Serializer):
            msg = (
                'You passed a Serializer instance as data, but '
                'probably meant to pass serialized `.data` or '
                '`.error`. representation.'
            )
            raise AssertionError(msg)

        self.cached_headers = headers
        self.cached_status = status
        self.cached_data = self.data = data
        self.exception = exception
        self.template_name = template_name
        self.content_type = content_type
        self.biz = biz

        self.error_code = error_code
        self.error_message = error_message

        if self.exception:
            self.handle_exception(error_code, error_message)
        else:
            self.handle_normal()

        if headers:
            for name, value in six.iteritems(headers):
                self[name] = value

    def handle_normal(self):
        if self.biz:
            self.data = {'response': self.data or {},
                         'error_code': '0',
                         'error_message': ''}

    def handle_exception(self, error_code, error_message=None):
        if self.biz:
            if error_message is None:
                error_message = ERROR_PHRASES.get(error_code, '')

            ret = {
                'error_code': error_code,
                'error_message': error_message
            }

            if self.data:
                ret['error_data'] = self.data

            self.data = ret