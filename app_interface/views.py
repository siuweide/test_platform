import json
import requests
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


# 获取项目/模块的数据
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

        return JsonResponse({"status": 10200, "message": "success", "data": data_list})

# 发送接口
def send_req(request):
    if request.method == "GET":
        url = request.GET.get("url", "")
        method = request.GET.get("method", "")
        header = request.GET.get("header", "")
        per_type = request.GET.get("per_type", "")
        per_value = request.GET.get("per_value", "")

        try:
            header = json.load(header)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"status": 10201, "message": "header必须为json格式"})

        try:
            per_value = json.load(per_value)
        except json.decoder.JSONDecodeError:
            return JsonResponse({"status": 10202, "message": "per_value必须为json格式"})

        res = ""

        if method == "get":
            if per_type == "form":
                res = requests.get(url, params=per_value, headers=header)
            elif per_type == "json":
                res = requests.get(url, json=per_value, headers=header)
        elif method == "post":
            if per_type == "form":
                res = requests.post(url, data=per_value, headers=header)
            elif per_type == "json":
                res = requests.post(url, json=per_value, headers=header)
        return JsonResponse({"status": 10200, "message": "success", "data": res.json()})