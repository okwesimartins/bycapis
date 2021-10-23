from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import  DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.forms import ModelForm 
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import CreateUserForm
from django.contrib.auth import login
from .models import Task
# Create your views here.
class customLoginview(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class Registerpage(FormView):
    template_name = 'base/register.html'
    form_class = CreateUserForm
    redirect_authenticated_user = True 
    success_url = reverse_lazy('login')            
    
    def form_valid(self, form):
        user = form.save()
        
        return super(Registerpage, self).form_valid(form)
    
    def get(self, *args,**kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(Registerpage,self).get(*args,**kwargs)
class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)
        
        context['search_input'] = search_input

        return context

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'tasks'

class TaskCreate(LoginRequiredMixin,CreateView):
    model= Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields =  ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

class Deletetask(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
