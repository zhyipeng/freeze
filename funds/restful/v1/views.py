from rest_framework.decorators import action
from rest_framework.exceptions import ValidationError

from core import exceptions
from core.exceptions import handle_validation_error_msg
from core.responses import Response
from core.viewsets import BaseViewSet
from funds.models import Fund
from funds.restful.v1.forms import AddConcernedFundForm


class FundViewSet(BaseViewSet):
    queryset = Fund.objects.all()

    @action(methods=['post'], detail=False)
    def add_concern_fund(self, request):
        form = AddConcernedFundForm(data=request.data,
                                    context=self.get_serializer_context())
        try:
            form.is_valid(raise_exception=True)
            form.save()

            return Response()
        except ValidationError as e:
            err_msg = handle_validation_error_msg(e.get_full_details())

        except exceptions.BusinessException as e:
            err_msg = e.err_msg

        return Response(error_message=err_msg, exception=True)
