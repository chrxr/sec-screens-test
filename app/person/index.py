from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Person

@register(Person)
class YourModelIndex(AlgoliaIndex):
    fields = ('fullname', 'fullnameOverride', 'location', 'locationOverride')
    settings = {'searchableAttributes': ['fullname', 'fullnameOverride']}
    index_name = 'person_index'