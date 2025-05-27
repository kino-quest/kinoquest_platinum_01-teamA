from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('privacy/', views.privacy, name="privacy"),
    path('rules/', views.rules, name="rules"),
    path('add_task/', views.add_task, name="add_task"),
    path('update_task/<int:task_id>/', views.update_task, name="update_task"),
    path('delete_task/<int:task_id>/', views.delete_task, name="delete_task"),
    path('solve_task/<int:task_id>/', views.solve_task, name="solve_task"),
]
