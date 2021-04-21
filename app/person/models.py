from django.db import models

# Create your models here.

class Person(models.Model):
  eppn = models.CharField(max_length=255, null=True, blank=True, verbose_name='EPPN')
  firstname = models.CharField(max_length=255, null=True, blank=True, verbose_name="First name")
  lastname = models.CharField(max_length=255, null=True, blank=True, verbose_name='Last name')
  location = models.CharField(max_length=255, null=True, blank=True, verbose_name='Location')
  fullname = models.CharField(max_length=255, null=True, blank=True, verbose_name='Full name')
  firstnameOverride = models.CharField(max_length=255, null=True, blank=True, verbose_name='First name (override)')
  lastnameOverride = models.CharField(max_length=255, null=True, blank=True, verbose_name='Last name (override')
  locationOverride = models.CharField(max_length=255, null=True, blank=True, verbose_name='Location (override)')
  fullnameOverride = models.CharField(max_length=255, null=True, blank=True, verbose_name='Full name (override)')

  def __str__(self):
    if self.fullnameOverride:
      return self.fullnameOverride
    else:
      return self.fullname
