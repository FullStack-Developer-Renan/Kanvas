from django.db import models
from django.db.models.fields.related import ForeignKey
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=255, unique=True)
    users = models.ManyToManyField(User)

class Activity(models.Model):
    title = models.CharField(max_length=255, unique=True)
    points = models.FloatField()

class Submission(models.Model):
    grade = models.FloatField(null=True)
    repo = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    
    def user_serializer(self):
        return {"user": self.user.id}
    
    def activity_serializer(self):
        return {"activity": self.activity.id}

    def __repr__(self):
        return str(self.__dict__)
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