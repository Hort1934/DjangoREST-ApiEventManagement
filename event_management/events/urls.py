from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EventViewSet, UserCreateView

router = DefaultRouter()
router.register(r'events', EventViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/register/', UserCreateView.as_view(), name='register'),
]
