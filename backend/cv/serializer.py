from rest_framework import serializers
from .models import Degree

class DegreeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Degree
        fields = ['name']