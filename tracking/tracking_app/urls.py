from django.urls import path, include
from .views import *

urlpatterns = [
    path('task-list', TaskListView.as_view(), name='task_list'),
    path('task-create', TaskCreateView.as_view(), name='create_task'),
    path('task-update', TaskUpdateView.as_view(), name='update_task'),
    path('task-detail', TaskDetailView.as_view(), name='task_detail'),
    path('task-delete', TaskDeleteView.as_view(), name='delete_task'),
    path('register', RegisterView.as_view(), name='register')
]