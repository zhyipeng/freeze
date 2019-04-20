from django.shortcuts import render
from django.views import View


class BasePageView(View):
    template = 'funds/index.html'
    form = None

    def get(self, request):
        return render(request, self.template)

    def get_serializer_context(self):
        return {
            'user': self.request.session['user'],
            'request': self.request
        }
