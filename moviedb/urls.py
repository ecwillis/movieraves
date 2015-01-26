from django.conf.urls import patterns, url
from moviedb import views

urlpatterns = patterns('',
  url(r'^movies/$', views.movie_index, name='movie_index'),
  url(r'^movie/(?P<movie_slug>[A-Za-z\-_]+)/$', views.movie, name='movie'),
  url(r'^actors/$', views.actor_index, name='actor_index'),
  url(r'^actor/(?P<actor_slug>[A-Za-z\-_]+)/$', views.actor, name='actor'),
)