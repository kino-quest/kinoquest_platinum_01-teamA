from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('privacy/', views.privacy, name="privacy"),
    path('rules/', views.rules, name="rules"),
    path('add_task/', views.add_task, name="add_task"),
]
