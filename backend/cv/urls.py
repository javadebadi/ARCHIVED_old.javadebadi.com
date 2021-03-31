from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import DegreeViewSet

router = DefaultRouter()
router.register('degrees', DegreeViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]
