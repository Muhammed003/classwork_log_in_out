from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import ProductAPIView, ProductSetView

router = SimpleRouter()
router.register('', ProductSetView)

urlpatterns = [
    path("product/", include(router.urls)),
    path("lists/", ProductAPIView.as_view()),
]

