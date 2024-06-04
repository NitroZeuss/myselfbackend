from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('message', views.messageViewSet, basename='message')
router.urls

urlpatterns = router.urls
