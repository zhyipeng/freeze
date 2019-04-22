from django.urls import path

from funds import views

urlpatterns = [
    path('', views.FundView.as_view(), name='index'),
    path('mine/concerned_funds',
         views.ConcernedFundView.as_view(),
         name='concerned'),
    path('mine/add_fund',
         views.AddConcernedFundView.as_view(),
         name='add_fund'),
    path('mine/add_data', views.AddFundDataView.as_view(), name='add_data'),
    path('mine/<int:pk>/add_data', views.AddFundData2View.as_view(), name='add_data2'),
]
