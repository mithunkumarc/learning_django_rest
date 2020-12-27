from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Musician, Album
# Register your models here.
#admin.site.register(Event)

@admin.register(Musician)
class MusicianAdmin(admin.ModelAdmin):
    # list all fields in table(Admin UI)
    # id : default field created by django
    list_display = ['id', 'first_name', 'last_name', 'instrument']


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    # list all fields in table(Admin UI)
    # id : default field created by django
    list_display = ['id', 'artist', 'name', 'release_date', 'num_stars']
