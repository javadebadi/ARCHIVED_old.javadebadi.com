from rest_framework import viewsets
from .models import Degree
from .models import Education
from .serializer import DegreeSerializer
from .serializer import EducationSerializer

# Create your views here.
class DegreeViewSet(viewsets.ModelViewSet):
    queryset = Degree.objects.all()
    serializer_class = DegreeSerializer

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer