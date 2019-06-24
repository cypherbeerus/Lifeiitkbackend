from .views import LoginView, LogoutView, EditAPI
from django.urls import path

urlpatterns = [
    path('', EditAPI,name="edit"),
    path('auth/login/', LoginView.as_view(), name="auth-login"),
    path('auth/logout/', LogoutView.as_view(), name="auth-logout")
]
