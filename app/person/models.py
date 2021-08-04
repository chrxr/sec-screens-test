from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.admin.models import LogEntry

# Create your models here.

class FeedPerson(models.Model):
  eppn = models.CharField(max_length=255, null=True, blank=True, verbose_name='EPPN')
  firstname = models.CharField(max_length=255, null=True, blank=True, verbose_name="First name")
  lastname = models.CharField(max_length=255, null=True, blank=True, verbose_name='Last name')
  location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Location')
  name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Full name')


class Person(models.Model):
  firstname = models.CharField(max_length=255, null=True, blank=True, verbose_name="First name")
  lastname = models.CharField(max_length=255, null=True, blank=True, verbose_name='Last name')
  location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Location')
  name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Full name')

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    RefreshRollup()

class Place(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True, verbose_name="First name")
  location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Location')

  def save(self, *args, **kwargs):
    super().save(*args, **kwargs)
    RefreshRollup()

class Rollup(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True)
  location = models.CharField(max_length=255, null=True, blank=True)

### Tests for RefreshRollup:
# * Does the function clear out any old objects?
# * Does the function correctly translate all of the existing database objects into the rollup model?

def RefreshRollup():
  Rollup.objects.all().delete()
  FeedPeople = FeedPerson.objects.all()
  People = Person.objects.all()
  Places = Place.objects.all()
  
  for objects in [FeedPeople, People, Places]:
    for object in objects:
      Rollup.objects.create(
        name = object.name,
        location = object.location
      )