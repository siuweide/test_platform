from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from app_manage.models import Project
from app_manage.form import ProjectForm

# 列表
def list(request):
    projectList = Project.objects.all()
    p = Paginator(projectList, 5)
    page = request.GET.get('page', '')
    if page == '':
        page = 1
    try:
        projectList = p.page(page)
    except PageNotAnInteger:
        projectList = p.page(1)
    except EmptyPage:
        projectList = p.page(p.num_pages)
    return render(request, 'project/list.html', {
        'projectList': projectList
    })

# 创建项目
def add(request):
    if request.method == 'GET':
        forms = ProjectForm()
        return render(request, 'project/add.html', {
            'forms': forms
        })
    else:
        forms = ProjectForm(request.POST)
        if forms.is_valid():
            name = forms.cleaned_data['name']
            describe = forms.cleaned_data['describe']
            status = forms.cleaned_data['status']
            Project.objects.create(name=name,
                                   describe=describe,
                                   status=status)
            return redirect('list_project')
        else:
            return render(request, 'project/add.html', {
                'forms': forms
            })

# 编辑项目
def edit(request, pid):
    if pid:
        project = Project.objects.get(id=pid)
        if request.method == 'GET':
            forms = ProjectForm(instance=project)
            return render(request, 'project/edit.html', {
                'forms': forms,
                'pid': pid,
            })
        else:
            forms = ProjectForm(request.POST)
            if forms.is_valid():
                name = forms.cleaned_data['name']
                describe = forms.cleaned_data['describe']
                status = forms.cleaned_data['status']

                project.name = name
                project.describe = describe
                project.status = status

                project.save()

                return redirect('list_project')
            return render(request, 'project/edit.html', {
                'forms': forms,
                'pid': pid,
            })

# 删除项目
def delete(request, pid):
    if pid:
        if request.method == 'GET':
            project = Project.objects.get(id=pid)
            project.delete()
            return redirect('list_project')

