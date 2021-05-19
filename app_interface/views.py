from django.http import JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from app_interface.models import ApiCase
from app_manage.models import Project, Module

def list(request):
    api_list = ApiCase.objects.all()
    p = Paginator(api_list, 5)
    page = request.GET.get('page', '')
    if page == '':
        page = 1
    try:
        api_list = p.page(page)
    except PageNotAnInteger:
        api_list = p.page(1)
    except EmptyPage:
        api_list = p.num_pages
    return render(request, 'interface/list.html', {
        'api_list': api_list
    })


def add(request):
    return render(request, 'interface/add.html')


def get_select_data(request):
    if request.method == "GET":
        projects = Project.objects.all()
        data_list = []
        for p in projects:
            project_dict = {
                "id": p.id,
                "name": p.name
            }
            modules = Module.objects.filter(project=p.id)
            module_list = []
            for m in modules:
                module_dict = {
                    "id": m.id,
                    "name": m.name
                }
                module_list.append(module_dict)
            project_dict['moduleList'] = module_list
            data_list.append(project_dict)

        return JsonResponse({"data": data_list})

