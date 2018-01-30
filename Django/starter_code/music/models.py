from django.db import models


class Muscician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    artist_age = models.IntegerField()

    def __str__(self):
        return self.first_name + " " + self.last_name

class Album(models.Model):
    artist =  models.ForeignKey(Muscician, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
            return self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=250)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.song_name + '.' + self.file_type
