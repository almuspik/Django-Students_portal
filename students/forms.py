from django import forms
from .models import Student

YEAR_CHOICES = [(1, '1st Year'), (2, '2nd Year'), (3, '3rd Year'), (4, '4th Year')]

class StudentForm(forms.ModelForm):
    studying_year = forms.ChoiceField(choices=YEAR_CHOICES)

    class Meta:
        model = Student
        fields = ['reg_no', 'name', 'age', 'department', 'studying_year', 'photo']
