from django.urls import path
from app_interface import views

urlpatterns = [
    path('list/', views.list, name='list_apicase'),
    path('add/', views.add, name='add_apicase')
]