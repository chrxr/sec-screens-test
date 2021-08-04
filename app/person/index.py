from algoliasearch_django import AlgoliaIndex
from algoliasearch_django.decorators import register

from .models import Rollup

@register(Rollup)
class YourModelIndex(AlgoliaIndex):
    fields = ('name', 'location')
    settings = {'searchableAttributes': ['name']}
    index_name = 'person_index'