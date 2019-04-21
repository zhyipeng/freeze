from django.urls import path

from funds import views

urlpatterns = [
    path('', views.FundView.as_view(), name='index'),
    path('mine/concerned_funds',
         views.ConcernedFundView.as_view(),
         name='concerned'),
    path('mine/add_fund',
         views.AddConcernedFundView.as_view(),
         name='add_fund')
]
