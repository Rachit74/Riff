from django.urls import path
from . import views

# api endpoint of tracks are /track/<urls>

urlpatterns = [
    path('upload/', views.UploadTrackView.as_view()),
    path('tracks/', views.GetAllTracks.as_view()),
]