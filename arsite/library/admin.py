"""Model registration for library app."""

# django
from django.contrib import admin

from .models import SearchQuery, Tag, Video

admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(SearchQuery)
