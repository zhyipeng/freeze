from rest_framework.routers import SimpleRouter

from funds.restful.v1.views import FundViewSet, InvestLogViewSet

router = SimpleRouter()
router.register('funds/api/v1', FundViewSet, base_name='')
router.register('funds/api/v1/invest_log',
                InvestLogViewSet,
                base_name='invest_log')

urlpatterns = router.urls
