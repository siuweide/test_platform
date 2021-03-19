
from django.urls import path

from app_manage.views import project_views

urlpatterns = [
    path('list/', project_views.list)
]