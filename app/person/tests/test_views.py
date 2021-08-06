from django.test import TestCase
from django.urls import reverse
from person.views import import_view
from person.models import FeedPerson, Rollup, Person, Place

class TestImportView(TestCase):

  def test_all_view_tests(self):
    
    # Test URL exists at the appropriate place
    response = self.client.get('/importer/upload/')
    self.assertEqual(response.status_code, 200)
    
    # Test Frank Doyle has been imported
    try:
      frank = FeedPerson.objects.get(name='Frank J. Doyle')
    except FeedPerson.DoesNotExist:
      frank = False

    self.assertTrue(frank)

    # Test that all of the FeedPerson records have been imported into Rollup
    feed_people = FeedPerson.objects.all()
    rollup_people = Rollup.objects.all()

    self.assertTrue(len(feed_people), len(rollup_people))