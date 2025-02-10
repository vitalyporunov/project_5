from django import forms
from .models import Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description', 'start_date', 'end_date', 'stakeholders', 'status']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),  # ✅ Calendar for Start Date
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),    # ✅ Calendar for End Date
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'stakeholders': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
