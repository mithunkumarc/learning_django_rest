from django.contrib import admin
from .models import Event
# Register your models here.
#admin.site.register(Event)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # list all fields in table(Admin UI)
    # id : default field created by django
    list_display = ['id', 'title', 'place', 'city', 'state', 'zipcode']
