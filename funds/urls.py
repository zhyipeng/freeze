from django.urls import path

from funds import views

urlpatterns = [
    path('', views.FundView.as_view(), name='index'),
]
