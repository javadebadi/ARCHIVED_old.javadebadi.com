from django.db import models

# static table to include name of degrees
class Degree(models.Model):
    name = models.CharField(max_length=128, unique=True)
    owner_id = models.ForeignKey(to='auth.user', related_name='degrees', on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name

# a model to include title of jobs
class Job(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

# a model for countries
class Country(models.Model):
    name = models.CharField(max_length=128, unique=True)
    code = models.CharField(max_length=2, unique=True)

    def __str__(self):
        return self.name

# a model for city
class City(models.Model):
    name = models.CharField(max_length=128)
    country_id = models.ForeignKey(to=Country, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    

# a model to include companies info
class Company(models.Model):
    name = models.CharField(max_length=256)

    def __str__(self):
        return self.name

# a model to include details of schools
class School(models.Model):
    name = models.CharField(max_length=256)
    city_id = models.ForeignKey(to=City, on_delete=models.PROTECT)

    def __str__(self):
        return self.name
    
# a model to store education information such as schools and grades
class Education(models.Model):
    degree_id = models.ForeignKey(to=Degree, on_delete=models.PROTECT)
    school_id = models.ForeignKey(to=School, on_delete=models.PROTECT)
    study_field = models.CharField(max_length=128, null=True, blank=True, default="Science")
    thesis_title = models.CharField(max_length=256, null=True, blank=True, default=None)
    advisers = models.CharField(max_length=256, null=True, blank=True, default=None)
    gpa = models.FloatField(null=True, blank=True) # the GPA
    start_date = models.DateField(blank=False, null=False) # start date is not allowed to be null
    end_date = models.DateField(blank=False, null=True) # end date can be null
    description = models.TextField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return f'{self.degree_id} at {self.school_id}'

# a model to include job experiences    
class Experince(models.Model):
    job_id = models.ForeignKey(to=Job, on_delete=models.PROTECT)
    company_id = models.CharField(null=True, blank=True, max_length=256)
    start_date = models.DateField(blank=False, null=False) # start date is not allowed to be null
    end_date = models.DateField(blank=False, null=True) # end date can be null
    description = models.TextField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return f'{self.job_id} at {self.company_id}'
