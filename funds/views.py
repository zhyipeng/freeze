from django.db.models import Q

from core.mixins import LoginRequiredMixin
from core.views import BasePageView
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
