from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework.exceptions import ValidationError

from core.exceptions import BusinessException


class LoginRequiredMixin:

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('user'):
            return redirect(reverse('members:login'))

        return super().dispatch(request, *args, **kwargs)


class GenericFormPostMixin:

    def post(self, request):
        form = self.form(
            data=request.POST, context=self.get_serializer_context())

        try:
            form.is_valid(raise_exception=True)
            form.save()
            return render(request, self.template, {'msg': '添加成功'})

        except ValidationError as e:
            return render(
                request, self.template, {'err_msg': e.get_full_details()})

        except BusinessException as e:
            return render(request, self.template, {'err_msg': e.err_msg})

        except Exception:
            return render(request, self.template, {'err_msg': '未知错误'})