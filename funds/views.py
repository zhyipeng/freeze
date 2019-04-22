from django.db.models import Q
from django.shortcuts import redirect

from core.mixins import LoginRequiredMixin
from core.responses import response_or_error
from core.views import BasePageView, DetailPageView
from funds.forms import AddFundDataForm
from funds.models import Fund


class FundView(LoginRequiredMixin, BasePageView):
    template = 'funds/index.html'


class AddConcernedFundView(LoginRequiredMixin, BasePageView):
    template = 'funds/add_fund.html'

    def render_data(self):
        q = self.request.GET.get('q')
        if not q:
            return {'q': q}

        return {
            'funds': Fund.objects.filter(
                Q(name__contains=q) | Q(code__contains=q)),
            'q': q,
        }


class ConcernedFundView(LoginRequiredMixin, BasePageView):
    template = 'funds/concerned.html'

    def render_data(self):
        return {
            'funds': Fund.objects.filter(
                id__in=self.request.user.concerned_funds)
        }


class AddFundDataView(ConcernedFundView):
    template = 'funds/add_data.html'


class AddFundData2View(LoginRequiredMixin, DetailPageView):
    template = 'funds/add_data2.html'
    queryset = Fund.objects.all()

    def post(self, request, pk):
        data = {
            'fund_id': pk,
            'value': request.POST.get('value'),
            'date': request.POST.get('date')
        }
        print(data)
        form = AddFundDataForm(data=data,
                               context=self.get_serializer_context())

        err_msg = response_or_error(form)
        return redirect(f'/mine/{pk}/add_data?err_msg={err_msg}')
