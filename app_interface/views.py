from django.shortcuts import render
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from app_interface.models import ApiCase

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