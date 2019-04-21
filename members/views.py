from django.shortcuts import render, redirect
from django.urls import reverse
from rest_framework.exceptions import ValidationError

from core.exceptions import handle_validation_error_msg
from core.mixins import LoginRequiredMixin
from core.views import BasePageView
from members.forms import LoginForm, RegisterForm


class MineView(LoginRequiredMixin, BasePageView):
    template = 'members/mine.html'


class LoginView(BasePageView):
    template = 'members/login.html'

    def post(self, request):
        form = LoginForm(data=request.POST)

        try:
            form.is_valid(raise_exception=True)
            user = form.save()
            request.session['user'] = user.id
            return redirect(reverse('funds:index'))
        except ValidationError as e:
            err_msg = handle_validation_error_msg(e.get_full_details())
            return render(request, self.template, {'err_msg': err_msg})


class RegisterView(BasePageView):
    template = 'members/register.html'

    def post(self, request):
        form = RegisterForm(data=request.POST)

        try:
            form.is_valid(raise_exception=True)
            user = form.save()
            if user:
                request.session['user'] = user.id

            return redirect(reverse('funds:index'))
        except ValidationError as e:
            err_msg = handle_validation_error_msg(e.get_full_details())
            return render(request, self.template, {'err_msg': err_msg})
