from django.urls import path, include
from .views import webhook_receiver, MessageViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('messages', MessageViewSet)

urlpatterns = [
    path('webhook/', webhook_receiver, name='webhook_receiver'),
    path('', include(router.urls)),
]