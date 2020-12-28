from django.contrib import admin
from .models import Vehicle, Car

# register your models here
# admin.site.register(Vehicle)
# admin.site.register(Car)

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    # list below fields in admin UI
    list_display= ['reg_no', 'owner']


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    # list below fields in admin UI
    list_display = ['vehicle', 'car_model']
