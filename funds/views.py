from core.mixins import LoginRequiredMixin, GenericFormPostMixin
from core.views import BasePageView
from funds.forms import AddConcernedFundForm


class FundView(LoginRequiredMixin, BasePageView):
    template = 'funds/index.html'


class AddConcernedFundView(LoginRequiredMixin, GenericFormPostMixin, BasePageView):
    template = 'funds/add_fund.html'
    form = AddConcernedFundForm
