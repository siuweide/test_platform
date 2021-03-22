from app_manage.models import Project
from django.shortcuts import render

# Create your views here.

def list(request):
    projectList = Project.objects.all()
    return render(request, 'project/list.html', {
        'projectList': projectList
    })