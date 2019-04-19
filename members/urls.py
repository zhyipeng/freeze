from django.urls import path

from members.views import MineView

urlpatterns = [
    path('mine', MineView.as_view(), name='mine'),
]