from django.shortcuts import render
from django.views import View

from members.models import User


class BasePageView(View):
    template = 'funds/index.html'
    queryset = None
    form = None

    def dispatch(self, request, *args, **kwargs):
        user_id = request.session.get('user')
        request.user = User.objects.filter(id=user_id).first()
        return super().dispatch(request, *args, **kwargs)

    def get(self, request):
        data = self.render_data()
        data['user'] = request.user
        data['err_msg'] = request.GET.get('err_msg', '')
        return render(request, self.template, data)

    def get_serializer_context(self):
        return {
            'user': self.request.user,
            'request': self.request
        }

    def render_data(self):
        return {}


class DetailPageView(BasePageView):

    def render_data(self, pk):
        return {}

    def get_object(self, pk):
        return self.queryset.filter(id=pk).first()

    def get(self, request, pk):
        data = self.render_data(pk)
        data['user'] = request.user
        data['instance'] = self.get_object(pk)
        data['err_msg'] = request.GET.get('err_msg', '')
        return render(request, self.template, data)
