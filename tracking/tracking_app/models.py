from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):

    status_choices = [
        ('todo', 'To Do'),
        ('pending', 'Pending'),
        ('finished', 'Finished'),
    ]

    priority_choices = [
        ('high', 'High'),
        ('medium', 'Medium'),
        ('low', 'Low'),
    ]

    title = models.CharField(max_length=255, name='Name')
    description = models.TextField(name='Description')
    status = models.CharField(max_length=20, choices=status_choices, name='Status')
    priority = models.CharField(max_length=20, choices=priority_choices, name='Priority')
    deadline = models.DateTimeField(null=True, blank=True, name='Deadline')
    user = models.ForeignKey(User, on_delete=models.CASCADE, name='User')

class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='task')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)