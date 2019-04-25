from django.db.models import Q
from django.shortcuts import redirect

from core.mixins import LoginRequiredMixin
from core.responses import get_error_message
from core.views import BasePageView, DetailPageView
from funds.forms import AddFundDataForm, AddInvestLogForm
from funds.models import Fund, InvestmentLog


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
        form = AddFundDataForm(data=data,
                               context=self.get_serializer_context())

        err_msg = get_error_message(form)
        return redirect(f'/mine/{pk}/add_data?err_msg={err_msg}')


class InvestLogView(ConcernedFundView):
    template = 'funds/invest_log.html'


class InvestLog2View(LoginRequiredMixin, DetailPageView):
    template = 'funds/invest_log2.html'
    queryset = Fund.objects.all()

    def render_data(self, pk):
        return {
            'invest_logs': InvestmentLog.objects.filter(
                user=self.request.user,
                fund=self.get_object(pk)).order_by('-date')
        }

    def post(self, request, pk):
        data = {
            'fund_id': pk,
            'value': request.POST.get('value'),
            'option': request.POST.get('option'),
            'date': request.POST.get('date'),
        }
        form = AddInvestLogForm(data=data,
                                context=self.get_serializer_context())

        err_msg = get_error_message(form)
        return redirect(f'/mine/{pk}/invest_log?err_msg={err_msg}')
