from rest_framework.viewsets import GenericViewSet

from core.authentications import LoginAuthentication


class BaseViewSet(GenericViewSet):
    authentication_classes = (LoginAuthentication,)

    def get_serializer_context(self):
        return {
            'user': self.request.user,
            'request': self.request
        }