from django.urls import path, include
from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='home'),
    path('task/create/', TaskCreate.as_view(), name='task_create'),
    path('task/<int:pk>/update/', TaskUpdate.as_view(), name='task_update'),
    path('task/<int:pk>/delete/', TaskDelete.as_view(), name='task_delete'),
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'), 
    path('logout/', logout_view, name='logout'),
]