from django.urls import path

from app_manage.views import project_views
from app_manage.views import module_views

urlpatterns = [
    # 项目管理
    path('project_list/', project_views.list, name='list_project'),
    path('project_add/', project_views.add, name='add_project'),
    path('project_edit/<int:pid>/', project_views.edit, name='edit_project'),
    path('project_delete/<int:pid>/', project_views.delete, name='delete_project'),

    # 模块管理
    path('module_list/', module_views.list, name='list_module'),
    path('module_add/', module_views.add, name='add_module')
]