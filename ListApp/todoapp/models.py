from django.db import models

class ToDoList(models.Model):
    content = models.TextField( max_length= 1000)
