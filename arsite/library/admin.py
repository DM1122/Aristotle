from django.contrib import admin
from .models import Tag, Video, SearchQuery


admin.site.register(Tag)
admin.site.register(Video)
admin.site.register(SearchQuery)
