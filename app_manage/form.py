from django.forms import ModelForm, Textarea, TextInput
from app_manage.models import Project, Module

MODULE = Module.objects.all()

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'describe', 'status']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'describe': Textarea(attrs={'class': 'form-control'})
        }

class ModuleForm(ModelForm):
    class Meta:
        model = Module
        fields = ['project', 'name', 'describe', 'status']
        widgets = {
            # 'project': SelectMultiple(),
            'name': TextInput(attrs={'class': 'form-control'}),
            'describe': Textarea(attrs={'class': 'form-control'}),
        }