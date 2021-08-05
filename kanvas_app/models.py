from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User)

    

# class Song(models.Model):
#     title = models.CharField(max_length=255)
#     artist = models.ForeignKey(Artist, on_delete=models.CASCADE, related_name="songs")

#     def __str__(self):
#         return self.title


# class Biography(models.Model):
#     description = models.TextField()
#     artist = models.OneToOneField(Artist, on_delete=models.CASCADE)


# class Playlist(models.Model):
#     title = models.CharField(max_length=255)
#     songs = models.ManyToManyField(Song)