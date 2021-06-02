#from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('locality/', views.locality, name='locality'),
    path('locality_detail/<int:locality_id>/', views.locality_detail, name='locality_detail'),
    path('locality_create/', views.locality_create, name='locality_create'),
    path('locality_edit/<int:num>', views.locality_edit, name='locality_edit'),
    path('locality_delete/<int:num>', views.locality_delete, name='locality_delete'),
    path('locality_find', views.locality_find, name='locality_find'),
#以下を定義
    path('locality_photo/', views.photoupload, name='photoupload'),
]