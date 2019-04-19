from django.shortcuts import render
from django.views import View


class MineView(View):

    def get(self, request):
        return render(request, 'members/mine.html')
