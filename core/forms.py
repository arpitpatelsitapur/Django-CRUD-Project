from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name", "roll", "result_status")
        #fields = ("name", "roll", "department", "result_status")
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            #'department':forms.TextInput(attrs={'class':'form-control'}),
            'result_status':forms.TextInput(attrs={'class':'form-control'})
        }

