from person.models import FeedPerson, Person, Place, Rollup

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