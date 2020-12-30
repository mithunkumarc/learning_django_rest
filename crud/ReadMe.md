#### credits : https://dev.to/balt1794/django-rest-api-crud-tutorial-2894

        request.body vs request.data
        request.body : gives json data 
        request.data : gives serialized data (json converted to python object)

#### creating root project

        django-admin startproject eventmgmt

#### creating app

        cd eventmgmt
        python manage.py startapp event

#### add rest framwork and app to eventmgmt/settings.py

        INSTALLED_APPS = [
          ...
            'rest_framework',
            'event',
        ]


#### creating evnet model

        from django.db import models
        from datetime import datetime
        from django.utils.timezone import now

        # Create your models here.
        class Event(models.Model):
            class StateChoice(models.TextChoices):
                Alabama = 'Alabama, AL'
                Arizona = 'Arizona, AR'
                Wyoming = 'Wyoming, WY'

            title = models.CharField(max_length=50)
            place = models.CharField(max_length=50)
            city = models.CharField(max_length=50)
            state = models.CharField(
                max_length=50, choices = StateChoice.choices, default = StateChoice.Alabama
            )
            zipcode = models.CharField(max_length=10)
            other = models.CharField(max_length=50)
            start_date = models.CharField(max_length=50)
            end_date = models.CharField(max_length=50)
            category = models.CharField(max_length=25)
            list_date = models.DateTimeField(default=now, blank=True)

            class Meta:
                verbose_name_plural = 'events'

            def __str___(self):
                return self.title




#### register in event/admin.py


        from django.contrib import admin
        from .models import Event
        # Register your models here. one way to register
        # admin.site.register(Event)

        # second way to register event model to admin
        # customize to show fields
        @admin.register(Event)
        class EventAdmin(admin.ModelAdmin):
            # list all fields in table(Admin UI)
            # id : default field created by django
            list_display = ['id', 'title', 'place', 'city', 'state', 'zipcode']


#### prepare migrations, ( create schema )

        python manage.py makemigrations

#### apply migrations , ( create tables )

        python manage.py migrate

#### create admin user

        python manage.py createsuperuser
        admin 
        c0met123

#### run server 

        python manage.py runserver

#### create: event/serializers.py , views and model exchange data using serializers

        from rest_framework import serializers
        from .models import Event

        class EventSerializer(serializers.ModelSerializer):
            class Meta:
                model = Event
                fields = '__all__' # may be requesting to serialize all fields



#### handling request : views.py

          from django.shortcuts import render
          from rest_framework.response import Response
          from .models import Event
          from .serializers import EventSerializer
          from rest_framework.decorators import api_view
          from django.views.decorators.csrf import csrf_exempt
          import io
          from rest_framework.parsers import JSONParser
          # Create your views here.
          # get all events
          @api_view(['GET'])
          def eventList(request):
              events = Event.objects.all()
              serializer = EventSerializer(events, many=True)
              return Response(serializer.data)

          # get single event
          @api_view(['GET'])
          def eventDetail(request, pk):
              event = Event.objects.get(id=pk)
              serializer = EventSerializer(event, many=False)
              return Response(serializer.data)

          # create new event
          # @csrf_exempt
          @api_view(['POST'])
          def eventCreate(request):
              # convert incoming json to dictionary
              streamData = io.BytesIO(request.body)
              dictData = JSONParser().parse(streamData)
              serializer = EventSerializer(data=dictData)
              if serializer.is_valid():
                  serializer.save()
              else:
                  print('error while creating event', serializer.error_messages)
              return Response(serializer.data)


          # update
          @api_view(['PUT'])
          def eventUpdate(request, pk):
              event = Event.objects.get(id=pk)
              # read tobe update data sent by user
              streamData = io.BytesIO(request.body)
              dictData = JSONParser().parse(streamData)
              # instance : existing object data
              # data : tobe updated data
              serializer = EventSerializer(instance=event, data=dictData)
              if serializer.is_valid():
                  serializer.save()
              else:
                  print('error while creating event', serializer.error_messages)
              return Response(serializer.data)


          #delete user :
          @api_view(['DELETE'])
          def eventDelete(request, pk):
              event = Event.objects.get(id=pk)
              if event:
                  event.delete()
                  return Response('deleted')
              else:
                  return Response('error while deleting id : ',pk)




#### eventmgmt/urls.py

        from django.contrib import admin
        from django.urls import path
        from event import views
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', views.eventList, name='events'),
            path('event/<str:pk>', views.eventDetail, name='detail'),
            path('eventcreate/', views.eventCreate, name='create'),
            path('eventupdate/<str:pk>', views.eventUpdate, name='update'),
            path('eventdelete/<str:pk>', views.eventDelete ,name='delete'),
        ]


#### testing app

##### read all events ; 

        http://localhost:8000/admin
        create some events
        use postman : get all events : http://localhost:8000/



##### get single event detail

        http://localhost:8000/event/2



##### create event : post : localhost:8000/eventcreate/

          payload : 

              {
                  "title": "Memento",
                  "place": "memoryLand",
                  "city": "memorycity",
                  "state": "Wyoming, WY",
                  "zipcode": "2234",
                  "other": "some",
                  "start_date": "31/07/2019",
                  "end_date": "12/04/2020",
                  "category": "somecategory",
                  "list_date": "2020-12-27T12:38:12Z"
              }


        check in admin ui : http://localhost:8000/admin/event/event/


##### update : put : localhost:8000/eventupdate/3

          payload : 
          {
              "id": 3,
              "title": "interstellar",
              "place": "spaceland",
              "city": "spacecity",
              "state": "Wyoming, WY",
              "zipcode": "2234",
              "other": "some",
              "start_date": "31/07/2019",
              "end_date": "12/04/2020",
              "category": "somecategory",
              "list_date": "2020-12-27T12:38:12Z"
          }


###### delete event : request type : delete : localhost:8000/eventdelete/1
