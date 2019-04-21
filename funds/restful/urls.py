from rest_framework.routers import SimpleRouter

from funds.restful.v1.views import FundViewSet

router = SimpleRouter()
router.register('funds/api/v1', FundViewSet, base_name='')

urlpatterns = router.urls
