from django.shortcuts import render, redirect
from app_manage.models import Module
from app_manage.form import ModuleForm

def list(request):
    moduleList = Module.objects.all()
    return render(request, 'module/list.html/', {
        'moduleList': moduleList
    })


def add(request):
    if request.method == "GET":
        forms = ModuleForm()
        return render(request, 'module/add.html', {
            'forms': forms
        })
    else:
        forms = ModuleForm(request.POST)
        if forms.is_valid():
            project = forms.cleaned_data['project']
            name = forms.cleaned_data['name']
            describe = forms.cleaned_data['describe']

            Module.objects.create(project=project,
                                  name=name,
                                  describe=describe)
            return redirect('list_module')


def edit(request, mid):
    if request.method == "GET":
        if mid:
            module = Module.objects.get(id=mid)
            forms = ModuleForm(instance=module)
            return render(request, 'module/edit.html', {
                'forms': forms,
                'mid': mid
            })
    else:
        forms = ModuleForm(request.POST)
        if forms.is_valid():
            md = Module.objects.get(id=mid)
            md.project = forms.cleaned_data['project']
            md.name = forms.cleaned_data['name']
            md.describe = forms.cleaned_data['describe']
            md.status = forms.cleaned_data['status']
            md.save()

            return redirect('list_module')

def delete(request, mid):
    if request.method == "GET":
        if mid:
            md = Module.objects.get(id=mid)
            md.delete()
            return redirect('list_module')


