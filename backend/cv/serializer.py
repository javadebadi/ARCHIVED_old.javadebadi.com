from rest_framework import serializers
from .models import Degree
from .models import Country
from .models import City
from .models import Education

class DegreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Degree
        fields = ['id','name']

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class EducationSerializer(serializers.ModelSerializer):
    degree_id = DegreeSerializer(many=False, read_only=True)
    class Meta:
        model = Education
        fields = '__all__'
        depth = 3