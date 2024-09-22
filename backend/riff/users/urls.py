from django.urls import path

from . import views

urlpatterns = [
    path('login/', view=views.LoginView.as_view()),
    path('register/', view=views.RegisterView.as_view()),
    path('profile/', views.ProfileView.as_view())
]