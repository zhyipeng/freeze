from django.shortcuts import render
from django.views import View

from members.models import User


class BasePageView(View):
    template = 'funds/index.html'
    form = None

    def dispatch(self, request, *args, **kwargs):
        user_id = request.session.get('user')
        request.user = User.objects.filter(id=user_id).first()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = self.render_data()
        data['user'] = request.user
        return render(request, self.template, data)

    def get_serializer_context(self):
        return {
            'user': self.request.user,
            'request': self.request
        }

    def render_data(self):
        return {}