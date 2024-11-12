from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from tracking_app.models import User, Task, Comment
from django import forms

class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields

class UserAuthForm(AuthenticationForm):
    class Meta:
        model = User

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ["title", "description", "status", "priority", "deadline", "user"]

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comments']
