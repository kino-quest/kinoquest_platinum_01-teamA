from django.urls import path
from . import views

urlpatterns = [
    # 'accounts_app/signup'
    path('signup/', views.signup, name='signup'),
]
