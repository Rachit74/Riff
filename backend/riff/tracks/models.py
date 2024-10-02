from django.db import models
from users.models import Client
from django.conf import settings

# Create your models here.
class Track(models.Model):
    title = models.CharField(max_length=20, null=False)
    track_file = models.FileField(upload_to=settings.TRACKS_DIR, blank=False, null=False)
    track_cover = models.ImageField(upload_to=settings.TRACKS_COVERS_DIR, blank=False, null=False)
    realeased = models.DateField(auto_now_add=True)
    artist = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} by {self.artist}"