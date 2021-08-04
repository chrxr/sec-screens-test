from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib.request
import os
from django.db import models
from person.models import FeedPerson, RefreshRollup


# Create your views here.

def import_view(request):

  with urllib.request.urlopen('https://nodefeeds.seas.harvard.edu/app/api/person/list/all') as f:
    data = f.read().decode('utf-8')

  soup = BeautifulSoup(data, 'xml')

  people = soup.find_all('person')

  for person in people:
    if len(person.location.fordisp.text) > 0:
      if person.eppn.text:
        obj, created = FeedPerson.objects.update_or_create(
          eppn=person.eppn.text,
          defaults={
            'firstname': person.givenname.text,
            'lastname': person.lastname.text,
            'name': person.gecos.text,
            'location': person.location.fordisp.text,
          }
        )
        print(created)
  RefreshRollup()
      

