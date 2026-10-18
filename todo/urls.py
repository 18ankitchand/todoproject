from . import views
from django.urls import path


app_name= 'todo'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('logout/', views.signout, name='logout'),
    path('task_list', views.task_list, name='task_list'),
    path('add/', views.task_create, name='task_create'),
    path('edit/<int:pk>', views.task_update, name='task_update'),
    path('delete/<int:pk>', views.task_delete, name='task_delete'),
    path('toggle/<int:pk>', views.task_toggle, name='task_toggle'),
]
