from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'stakeholders', 'status']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),  
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),    

            # ✅ Fixed: Use SelectMultiple for ManyToManyField
            'stakeholders': forms.SelectMultiple(attrs={'class': 'form-control'}),  

            # ✅ Dropdown for status
            'status': forms.Select(attrs={'class': 'form-control'}),
        }

