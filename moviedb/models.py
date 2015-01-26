from django.db import models

# Create your models here.

class Movie(models.Model):

  def __unicode__(self):
    return self.title

  """ Field Definitions """

  title = models.CharField(max_length=255)
  slug = models.SlugField(max_length=255)
  description = models.TextField()
  plot_tag = models.CharField(max_length=255)
  rating = models.IntegerField(default=0)
  release_date = models.DateTimeField(null=True)
  running_time = models.IntegerField(default=0)
  status = models.SmallIntegerField(default=0)
  active = models.BooleanField(default=False)
  imdb_id = models.CharField(max_length=20)

class Actor(models.Model):

  def __unicode__(self):
    return self.name

  """ Field Definitions """

  name = models.CharField(max_length=255)
  slug = models.CharField(max_length=255)
  bio = models.TextField()
  title = models.CharField(max_length=255)
  birthdate = models.DateField(null=True)

class Character(models.Model):

  def __unicode__(self):
    return self.name

  """ Field Definitions """

  name = models.CharField(max_length=255)
  slug = models.CharField(max_length=255)
  description = models.TextField()
  actor = models.ForeignKey(Actor)
  movie = models.ForeignKey(Movie)