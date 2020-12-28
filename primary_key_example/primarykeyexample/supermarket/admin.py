from django.contrib import admin
from .models import Fruit
# Register your models here.
# admin.site.register(Fruit)

@admin.register(Fruit)
class FruitAdmin(admin.ModelAdmin):
    # list all fields in table(Admin UI)
    list_display = ['name']
