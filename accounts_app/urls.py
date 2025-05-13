from django.urls import path
from . import views

urlpatterns = [
    # 'accounts_app/signup'
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
]
