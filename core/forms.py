from django import forms
from .models import Student

class AddStudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = ("name", "roll", "department", "semester","total", "earned", "sgpa", "result_status")
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'roll':forms.NumberInput(attrs={'class':'form-control'}),
            'department':forms.TextInput(attrs={'class':'form-control'}),
            'semester':forms.NumberInput(attrs={'class':'form-control'}),
            'total':forms.NumberInput(attrs={'class':'form-control'}),
            'earned':forms.NumberInput(attrs={'class':'form-control'}),
            'sgpa':forms.NumberInput(attrs={'class':'form-control'}),
            'result_status':forms.TextInput(attrs={'class':'form-control'})
        }

