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

class Place(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True, verbose_name="Name")
  location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Location')

class Rollup(models.Model):
  name = models.CharField(max_length=255, null=True, blank=True)
  location = models.CharField(max_length=255, null=True, blank=True)