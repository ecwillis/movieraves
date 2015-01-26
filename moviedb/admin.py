from django.contrib import admin
from moviedb.models import Movie, Actor, Character
# Register your models here.

class MovieAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields' : ['title', 'slug', 'plot_tag', 'description', 'rating']}),
    ('Release Informaion', {'fields': ['release_date', 'running_time']}),
    ('State', {'fields': ['status', 'active']}),
  ]
admin.site.register(Movie, MovieAdmin)

class ActorAdmin(admin.ModelAdmin):
  """ Actor administration class """

admin.site.register(Actor, ActorAdmin)

admin.site.register(Character)