from django.db import models

# Create your models here.
from django.db import models

class Student(models.Model):
    reg_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    department = models.CharField(max_length=100)
    studying_year = models.PositiveIntegerField()
    photo = models.ImageField(upload_to='student_photos/', null=True, blank=True)  


    def __str__(self):
        return f"{self.name} ({self.reg_no})"
