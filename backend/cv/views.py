from rest_framework import generics
from .models import Degree
from .serializer import DegreeSerializer

# Create your views here.
class DegreeList(generics.ListCreateAPIView):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer