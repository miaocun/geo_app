#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('collector/', views.collector, name='collector'),
    path('collector_detail/<int:collector_id>/',views.collector_detail, name='collector_detail'),
    path('collector_create/', views.collector_create, name='collector_create'),
    path('collector_edit/<int:num>', views.collector_edit, name='collector_edit'),
    path('collector_delete/<int:num>', views.collector_delete, name='collector_delete'),
    path('collector_find', views.collector_find, name='collector_find'),
]
