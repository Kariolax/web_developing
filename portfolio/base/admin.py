from django.contrib import admin

# Register your models here.

from .models import Entry, Topic, Link

admin.site.register(Entry)
admin.site.register(Topic)
admin.site.register(Link)
