from rest_framework.authentication import BaseAuthentication

from members.models import User


def login_authenticate(request):
    user_id = request.session.get('user')
    user = User.objects.filter(id=user_id).first()


    return user, None


class LoginAuthentication(BaseAuthentication):

    def authenticate(self, request):
        return login_authenticate(request)
