from django.forms import ModelForm, Textarea, TextInput
from django.forms import widgets
from app_manage.models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'describe': Textarea(attrs={'class': 'form-control'})
        }
