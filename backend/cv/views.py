from rest_framework import viewsets
from .models import Degree
from .serializer import DegreeSerializer

# Create your views here.
class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer