from django.http import HttpResponse
from django.template import RequestContext, loader
from moviedb.models import Movie, Actor
from django.shortcuts import render

def movie_index(request):
  all_movies = Movie.objects.all()
  template = loader.get_template('moviedb/movie_index.html')
  context = { 'all_movies': all_movies }

  return render(request, 'moviedb/movie_index.html', context)

def movie(request, movie_slug):
  return HttpResponse("You're looking at the movie: %s." % movie_slug)

def actor_index(request):
  all_actors = Actor.objects.all()
  output = ', '.join([a.name for a in all_actors])
  return HttpResponse(output)

def actor(request, actor_slug):
  return HttpResponse("You are looking at the actor: %s" % actor_slug)