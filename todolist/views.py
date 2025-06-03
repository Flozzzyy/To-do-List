from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from.models import  *
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect

# Create your views here.

class Login(LoginView):
    template_name = 'todolist/login.html'
    success_url = reverse_lazy('home')

    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password')
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Successfully logged in')
        return super().form_valid(form)

def logout_view(request):
    logout(request)
    messages.success(request, 'Successfully logged out')
    return redirect('home')

class Register(CreateView):
    model = User
    template_name = 'todolist/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully! Please login.')
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, 'Please correct the errors below')
        return super().form_invalid(form)
    def help_text(self, form):
        form.fields['username'].help_text = None
        form.fields['password1'].help_text = None
        form.fields['password2'].help_text = None
        
class TaskList(ListView):
    model = Task
    template_name = 'todolist/home.html'
    context_object_name = 'tasks'
    
    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Task.objects.filter(user=self.request.user)
        return Task.objects.none()

class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'todolist/task_form.html'
    fields = ['name', 'status']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, 'Task created successfully!')
        return super().form_valid(form)

class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    template_name = 'todolist/task_form.html'
    fields = ['name', 'status']
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def form_valid(self, form):
        messages.success(self.request, 'Task updated successfully!')
        return super().form_valid(form)

class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('home')

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        messages.success(self.request, 'Task deleted successfully!')
        return HttpResponseRedirect(success_url)

