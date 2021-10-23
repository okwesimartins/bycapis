from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate,TaskUpdate,Deletetask,customLoginview, Registerpage
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('login/', customLoginview.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register', Registerpage.as_view(), name='register'),


    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>', TaskDetail.as_view(), name='task'),
    path('create-task/', TaskCreate.as_view(), name='task-create'),
    path('task-update/<int:pk>', TaskUpdate.as_view(), name='task-update'),
    path('task-delete/<int:pk>', Deletetask.as_view(), name='task-delete'),
]