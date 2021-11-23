from django.contrib import admin
from django.urls import path
from . import views 
from django.conf.urls import url


urlpatterns = [
    path('addTodoItem/', views.addToDoView),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView),
    url(r'^$', views.todoappView, name='index'),
]