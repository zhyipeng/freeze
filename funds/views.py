from django.shortcuts import render
from django.views import View


class FundView(View):

    def get(self, request):
        return render(request, 'funds/index.html')
