from django.test import TestCase
from person.models import Person, FeedPerson, Place, Rollup

class TestPersonModel(TestCase):
  @classmethod
  def setUpTestData(cls):
    Person.objects.create(
      name="Bob Dob",
      firstname="Bob",
      lastname="Dob",
      location="Here"
    )
    pass

  def test_person_name_max_length(self):
    person = Person.objects.get(id=1)
    max_length = person._meta.get_field('name').max_length
    self.assertEqual(max_length, 255)

  def test_person_firstname_max_length(self):
    person = Person.objects.get(id=1)
    max_length = person._meta.get_field('firstname').max_length
    self.assertEqual(max_length, 255)

  def test_person_lastname_max_length(self):
    person = Person.objects.get(id=1)
    max_length = person._meta.get_field('lastname').max_length
    self.assertEqual(max_length, 255)

  def test_person_location_max_length(self):
    person = Person.objects.get(id=1)
    max_length = person._meta.get_field('location').max_length
    self.assertEqual(max_length, 255)

  def test_person_name_label(self):
    person = Person.objects.get(id=1)
    field_label = person._meta.get_field('name').verbose_name
    self.assertEqual(field_label, "Full name")

  def test_person_firstname_label(self):
    person = Person.objects.get(id=1)
    field_label = person._meta.get_field('firstname').verbose_name
    self.assertEqual(field_label, "First name")

  def test_person_lastname_label(self):
    person = Person.objects.get(id=1)
    field_label = person._meta.get_field('lastname').verbose_name
    self.assertEqual(field_label, "Last name")

  def test_person_location_label(self):
    person = Person.objects.get(id=1)
    field_label = person._meta.get_field('location').verbose_name
    self.assertEqual(field_label, "Location")

class TestFeedPersonModel(TestCase):
  @classmethod
  def setUpTestData(cls):
    FeedPerson.objects.create(
      name="Bob Dob",
      firstname="Bob",
      lastname="Dob",
      location="Here",
      eppn="fjw30jf903wjg90wmg9"
    )

  def test_feedperson_name_max_length(self):
    feedperson = FeedPerson.objects.get(id=1)
    max_length = feedperson._meta.get_field('name').max_length
    self.assertEqual(max_length, 255)

  def test_feedperson_firstname_max_length(self):
    feedperson = FeedPerson.objects.get(id=1)
    max_length = feedperson._meta.get_field('firstname').max_length
    self.assertEqual(max_length, 255)

  def test_feedperson_lastname_max_length(self):
    feedperson = FeedPerson.objects.get(id=1)
    max_length = feedperson._meta.get_field('lastname').max_length
    self.assertEqual(max_length, 255)

  def test_feedperson_location_max_length(self):
    feedperson = FeedPerson.objects.get(id=1)
    max_length = feedperson._meta.get_field('location').max_length
    self.assertEqual(max_length, 255)

  def test_feedperson_location_label(self):
    feedperson = FeedPerson.objects.get(id=1)
    max_length = feedperson._meta.get_field('location').max_length
    self.assertEqual(max_length, 255)

  def test_feedperson_name_label(self):
    feedperson = FeedPerson.objects.get(id=1)
    field_label = feedperson._meta.get_field('name').verbose_name
    self.assertEqual(field_label, "Full name")

  def test_feedperson_firstname_label(self):
    feedperson = FeedPerson.objects.get(id=1)
    field_label = feedperson._meta.get_field('firstname').verbose_name
    self.assertEqual(field_label, "First name")

  def test_feedperson_lastname_label(self):
    feedperson = FeedPerson.objects.get(id=1)
    field_label = feedperson._meta.get_field('lastname').verbose_name
    self.assertEqual(field_label, "Last name")

  def test_feedperson_location_label(self):
    feedperson = FeedPerson.objects.get(id=1)
    field_label = feedperson._meta.get_field('location').verbose_name
    self.assertEqual(field_label, "Location")

  def test_feedperson_eppn_label(self):
    feedperson = FeedPerson.objects.get(id=1)
    field_label = feedperson._meta.get_field('eppn').verbose_name
    self.assertEqual(field_label, "EPPN")

class TestPlaceModel(TestCase):
  @classmethod
  def setUpTestData(cls):
      Place.objects.create(
        name="A lab",
        location="Here"
      )

  def test_place_name_max_length(self):
    place = Place.objects.get(id=1)
    max_length = place._meta.get_field('name').max_length
    self.assertEqual(max_length, 255)

  def test_place_location_label(self):
    place = Place.objects.get(id=1)
    max_length = place._meta.get_field('location').max_length
    self.assertEqual(max_length, 255)

  def test_place_name_label(self):
    place = Place.objects.get(id=1)
    field_label = place._meta.get_field('name').verbose_name
    self.assertEqual(field_label, "Name")

  def test_place_location_label(self):
    place = Place.objects.get(id=1)
    field_label = place._meta.get_field('location').verbose_name
    self.assertEqual(field_label, "Location")


class TestRollupModel(TestCase):
  @classmethod
  def setUpTestData(cls):
    Rollup.objects.create(
      name="A lab",
      location="Here"
    )

    def test_rollup_name_max_length(self):
      rollup = Rollup.objects.get(id=1)
      max_length = rollup._meta.get_field('name').max_length
      self.assertEqual(max_length, 255)

    def test_rollup_location_max_length(self):
      rollup = Rollup.objects.get(id=1)
      max_length = rollup._meta.get_field('location').max_length
      self.assertEqual(max_length, 255)