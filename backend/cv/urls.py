from django.urls import path
from .views import DegreeList

urlpatterns = [
    path('degrees/', DegreeList.as_view()),    
]
