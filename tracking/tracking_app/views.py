from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .mixins import *



# Create your views here. 
class TaskCreateView(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'templates/create_task.html'
    success_url = 'task-create'

class TaskUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'templates/update_task.html'
    success_url = 'task-detail'

class TaskListView(ListView):
    model = Task
    template_name = 'templates/task_list.html'
    content_object_name = None

    def task_list(request):
        tasks = Task.objects.all()
        status = request.GET.get('status')
        priority = request.GET.get('priority')
        deadline = request.GET.get('deadline')

        if status:
            tasks = tasks.filter(status=status)
        if priority:
            tasks = tasks.filter(priority=priority)
        if deadline:
            tasks = tasks.filter(deadline=deadline) 

        priorities = Task.objects.all() 
        return render(request, 'task_list.html', {
            'tasks': tasks,
            'priorities': priorities,
            'selected_status': status,
            'selected_priority': priority,
            'selected_deadline': deadline
        })

class TaskDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Task
    form_class = TaskForm
    template_name = 'templates/delete_task.html'
    success_url = 'task-create'

class TaskDetailView(DetailView):
    model = Task
    context_object_name = None
    template_name = 'templates/task_detail.view'

    def post(self, request, *args, **kwargs):
        form = CommentForm(request.POST)
        form.author = request.user
        form.task = self.get_object()

        if form.is_valid():
            form.save
        else:
            print("Invalid")
        return redirect('task-list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comments'] = Comment.objects.all()
        context['form'] = CommentForm
        return context

class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = "templates/register.html"

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('')