from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.LoginView.as_view()),
    path('register/', views.RegisterView.as_view()),
    path('profile/', views.ProfileView.as_view()),

    path('token/', views.TokenView.as_view()),
]