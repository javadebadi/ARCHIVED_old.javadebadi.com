from django.contrib import admin
from .models import Degree
from .models import Job
from .models import School
from .models import Company
from .models import Education
from .models import Experince
from .models import Country
from .models import City

# Register your models here.
admin.site.register(Degree)
admin.site.register(Job)
admin.site.register(School)
admin.site.register(Company)
admin.site.register(Education)
admin.site.register(Experince)
admin.site.register(City)
admin.site.register(Country)
