#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mission/', views.mission, name='mission'),
    path('mission_detail/<int:mission_id>/',views.mission_detail, name='mission_detail'),
    path('mission_create/', views.mission_create, name='mission_create'),
    path('mission_edit/<int:num>', views.mission_edit, name='mission_edit'),
    path('mission_delete/<int:num>', views.mission_delete, name='mission_delete'),
    path('mission_find', views.mission_find, name='mission_find'),
]
