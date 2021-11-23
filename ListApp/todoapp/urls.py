from django.contrib import admin
from django.urls import path
from . import views 


urlpatterns = [
    path('', views.todoappView, name='index'),
    path('addTodoItem/', views.addToDoView),
    path('deleteTodoItem/<int:i>/', views.deleteTodoView),
]