from django import forms
from . models import *

    
class testForm(forms.ModelForm):
    class Meta:
        model = test
        fields = ['name','startdate','enddate']
        widgets = {'startdate':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Select a date', 'type':'date'}),

        'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter a Name'}),
        'enddate':forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control','placeholder':'Select a date', 'type':'date'}),
        }