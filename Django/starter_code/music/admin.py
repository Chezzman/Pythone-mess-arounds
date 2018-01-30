from django.contrib import admin

from .models import Muscician, Album, Song

admin.site.register(Muscician)
admin.site.register(Album)
admin.site.register(Song)
