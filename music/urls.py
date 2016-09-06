from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # /music/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    # /music/songs
    url(r'^songs/$', views.Songs.as_view(), name='songs'),
    # /music/id/favorite
    url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    # /music/id/favorite_song
    url(r'^songs/(?P<song_id>[0-9]+)/favorite_song/$', views.favorite_song, name='favorite_song'),
    # /music/id/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    # /music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album-add'),
    # /music/song/add
    url(r'song/add/$', views.SongCreate.as_view(), name='song-add'),
    # /music/album/2
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album-update'),
    # /music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album-delete'),
]
