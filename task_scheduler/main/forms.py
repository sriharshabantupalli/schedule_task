from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Task


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=15)
    address = forms.CharField(max_length=255)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'mobile_number', 'address']


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['name', 'date_time', 'assigned_to']