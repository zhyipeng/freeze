from django.urls import path

from members import views

urlpatterns = [
    path('mine', views.MineView.as_view(), name='mine'),
    path('login', views.LoginView.as_view(), name='login'),
    path('register', views.RegisterView.as_view(), name='register'),
]