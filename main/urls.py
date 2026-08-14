from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
  path('', views.index, name='index'),
  path('projects/warehouse-manager/', views.warehouse_manager, name='warehouse_manager'),
  path('projects/rest-mgr/', views.rest_mgr, name='rest_mgr'),
]