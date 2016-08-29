from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=50)
    album_title = models.CharField(max_length=30)
    genre = models.CharField(max_length=30)
    album_logo = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.album_title + ', ' + self.artist + ', ' + self.genre


class Song(models.Model):
    song_title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
