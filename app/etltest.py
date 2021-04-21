from bs4 import BeautifulSoup
import urllib.request
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "app.settings.dev")

from django.db import models
from person.models import Person

# class Person:
#   def __init__(self, fullname, firstname, lastname, location):
#     self.fullname = fullname
#     self.firstname = firstname
#     self.lastname = lastname
#     self.location = location

with urllib.request.urlopen('https://nodefeeds.seas.harvard.edu/app/api/person/list/all') as f:
  data = f.read().decode('utf-8')

soup = BeautifulSoup(data, 'xml')

people = soup.find_all('person')

# people_list = []

for person in people:
  if len(person.location.fordisp) > 0:
    if person.eppn:
      print(person.eppn)
    else:
      print("nope")
    
    # obj, created = Person.objects.update_or_create(
    #   eppn=person.eppn,
    #   defaults={
    #     'firstname': person.givenname.text,
    #     'lastname': person.lastname.text,
    #     'fullname': person.gecos.text,
    #     'location': person.location.fordisp.text,
    #   }
    )
    print(created)
