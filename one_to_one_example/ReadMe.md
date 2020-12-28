## one to one relationship example
### one car --- one vehicle (owner) [ another car cannot share this vehicle(owner)]

### one car belongs to one owner(class Vehicle), or one owner(vehicle) can be mapped to only one car

        1. class Vehicle(owner) 
        2. class Car 
        creating/mapping two car for same vehicle(owner) raise error


#### test in admin UI, testing in postman not covered in this example


#### 1. create root project

        django-admin startproject onetooneexample
        
#### 2. create an app : showroom

        cd onetooneexample
        python manage.py startapp showroom

#### 3. onetooneexample/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'showroom',
        ]

#### 4. showroom/models.py

        from django.db import models 

        class Vehicle(models.Model): 
            reg_no = models.IntegerField() 
            owner = models.CharField(max_length = 100) 

        class Car(models.Model): 
            vehicle = models.OneToOneField(Vehicle,  
                  on_delete = models.CASCADE, primary_key = True) 
            car_model = models.CharField(max_length = 100) 





#### 5. register in showroom/admin.py 


        from django.contrib import admin
        from .models import Vehicle, Car
        # Register your models here.
        # admin.site.register(Vehicle)
        # admin.site.register(Car)

        @admin.register(Vehicle)
        class VehicleAdmin(admin.ModelAdmin):
            # list all fields in table(Admin UI)
            list_display = ['reg_no', 'owner']

        @admin.register(Vehicle)
        class CarAdmin(admin.ModelAdmin):
            # list all fields in table(Admin UI)
            list_display = ['vehicle', 'car_model']
	


#### 6. create and apply schema, creating superuser admin

        python manage.py makemigrations
        python manage.py migrate

        python manage.py createsuperuser
        admin 
        c0met123
        # run server
        python manage.py runserver


#### 7. testing : localhost:8000/admin

      1. create a vehicle(owner)
      2. create a car with a vehicle owner(mapping)
      3. create another car with existing vehicle owner(already mapped to other car) : raises error
       error : Car with this Vehicle already exists.


