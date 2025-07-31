from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('', views.TaskList.as_view(), name='home'),
    path('task/create/', views.TaskCreate.as_view(), name='create'),
    path('task/<int:pk>/', views.TaskDetail.as_view(), name='detail'),
    path('task/update/<int:pk>/', views.TaskUpdate.as_view(), name='update'),
    path('task/delete/<int:pk>/', views.TaskDelete.as_view(), name='delete'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

]
