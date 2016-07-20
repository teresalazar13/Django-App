from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_title + ', ' + self.artist + ", " + self.genre


class Song(models.Model):
    song_title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)

    def __str__(self):
        return self.song_title + ", " + self.album
