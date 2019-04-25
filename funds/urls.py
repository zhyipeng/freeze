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
    path('mine/<int:pk>/add_data',
         views.AddFundData2View.as_view(),
         name='add_data2'),
    path('mine/invest_log', views.InvestLogView.as_view(), name='invest_log'),
    path('mine/<int:pk>/invest_log',
         views.InvestLog2View.as_view(),
         name='invest_log2')
]
