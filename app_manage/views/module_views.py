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
            status = forms.cleaned_data['status']

            Module.objects.create(project=project,
                                  name=name,
                                  describe=describe,
                                  status=status)
            return redirect('list_module')
