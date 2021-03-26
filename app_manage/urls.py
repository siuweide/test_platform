from django.urls import path

from app_manage.views import project_views

urlpatterns = [
    path('list/', project_views.list, name='list_project'),
    path('add/', project_views.add, name='add_project'),
    path('edit/<int:pid>/', project_views.edit, name='edit_project'),
    path('delete/<int:pid>/', project_views.delete, name='delete_project'),
]