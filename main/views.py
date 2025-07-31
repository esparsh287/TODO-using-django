from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DeleteView,UpdateView, DetailView
from .models import Task
from django.urls import reverse_lazy




class TaskList(ListView):
  model= Task
  template_name='main/home.html'
  context_object_name='tasks'


class TaskDetail(DetailView):
  model= Task
  template_name='main/detail.html'
  context_object_name='task'


class TaskUpdate(UpdateView):
  model=Task
  template_name='main/update.html'
  fields='__all__'
  success_url=reverse_lazy('home')
  context_object_name='tasks'


class TaskDelete(DeleteView):
  model=Task
  template_name='main/delete.html'
  success_url=reverse_lazy('home')


class TaskCreate(CreateView):
  model=Task
  template_name='main/create.html'
  fields='__all__'
  success_url=reverse_lazy('home')


