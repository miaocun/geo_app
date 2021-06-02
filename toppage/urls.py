#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.top, name='top'),
    path('top_create', views.topcreate, name='topcreate'),
    path('edit/<int:num>', views.topedit, name='topedit'),
    path('delete/<int:num>', views.topdelete, name='topdelete'),
    path('top_find', views.topfind, name='topfind'),
]
