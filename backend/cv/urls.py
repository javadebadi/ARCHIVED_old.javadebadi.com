from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter
from .views import DegreeViewSet
from .views import EducationViewSet

router = DefaultRouter()
router.register('degrees', DegreeViewSet)
router.register('education', EducationViewSet)

urlpatterns = [
    path('', include(router.urls)),    
]
