from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView,CreateView,DeleteView,UpdateView, DetailView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin




class TaskList(ListView, LoginRequiredMixin):
  model= Task
  template_name='main/home.html'
  context_object_name='tasks'

  def get_queryset(self):
    return Task.objects.filter(user=self.request.user)


class TaskDetail(DetailView, LoginRequiredMixin):
  model= Task
  template_name='main/detail.html'
  context_object_name='task'


class TaskUpdate(UpdateView, LoginRequiredMixin):
  model=Task
  template_name='main/update.html'
  fields=['title','desc', 'date']
  success_url=reverse_lazy('home')
  context_object_name='tasks'


class TaskDelete(DeleteView, LoginRequiredMixin):
  model=Task
  template_name='main/delete.html'
  success_url=reverse_lazy('home')


class TaskCreate(CreateView, LoginRequiredMixin):
  model=Task
  template_name='main/create.html'
  fields=['title','desc', 'date']
  success_url=reverse_lazy('home')

  def form_valid(self, form):
    form.instance.user=self.request.user
    return super().form_valid(form)



class RegisterView(CreateView, LoginRequiredMixin):
  template_name='main/register.html'
  form_class=UserCreationForm
  success_url= reverse_lazy('login')


