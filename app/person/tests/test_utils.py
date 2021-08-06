from django.test import TestCase
from person.models import FeedPerson, Person, Place, Rollup
from person.utils.rollup import RefreshRollup

class TestRefreshRollup(TestCase):
  @classmethod
  def setUpTestData(cls):
    Person.objects.create(
      name = "Bob Dole",
      lastname = "Dole",
      firstname = "Bob",
      location = "Here"
    )

    FeedPerson.objects.create(
      name = "Bob Dole Feed",
      lastname = "Dole Feed",
      firstname = "Bob Feed",
      location = "Here Feed",
      eppn = "fniesnfioeqnfopqwnepo"
    )

    Place.objects.create(
      name = "Bod Dole place",
      location = "Here place",
    )

  def test_refreshrollup_clears_old_rollup(self):
    Rollup.objects.create(
      name = "This person has gone",
      location = "Somewhere"
    )

    RefreshRollup()

    try:
      dave = Rollup.objects.get(name="This person has gone")
    except Rollup.DoesNotExist:
      dave = False

    self.assertFalse(dave)

  def test_all_items_in_rollup(self):
    RefreshRollup()

    count = len(Rollup.objects.all())

    self.assertEqual(count, 3)

