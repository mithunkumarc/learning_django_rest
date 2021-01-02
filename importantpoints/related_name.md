related name is the field name of current object used by other related(1:1, 1:m, M:N) object 

#### sample

          
          Singer table : related_field="singer_info"
          Song table : uses "singer_info" to refer Singer table, by default it shows primary key of Singer record

#### example : lets look at models.py

        from django.db import models

        # Create your models here.
        class Singer(models.Model):
          name = models.CharField(max_length=100)
          gender = models.CharField(max_length=100)

        class Song(models.Model):
          title = models.CharField(max_length=100)
          # related name : sung is being used in SingerSerializer
          singer = models.ForeignKey(Singer, on_delete=models.CASCADE, related_name="sung")
          duration = models.IntegerField()

#### serializers.py

          from .models import Singer, Song
          from rest_framework import serializers


          class SongSerializer(serializers.ModelSerializer):
            class Meta:
              model = Song
              fields = ['id', 'title', 'singer', 'duration']


          class SingerSerializer(serializers.ModelSerializer):
            sung = SongSerializer(many=True, read_only=True)
            class Meta:
              model = Singer
              fields = ['id', 'name', 'gender', 'sung']     # using "sung" to show song details
              
              
#### output : example took from nested serializer, 

            [
                {
                    "id": 1,
                    "name": "subbanna",
                    "gender": "male",
                    "sung": [
                        {
                            "id": 1,
                            "title": "madikeri manju",
                            "singer": 1,
                            "duration": 3
                        }
                    ]
                },
                {
                    "id": 2,
                    "name": "jayashree",
                    "gender": "female",
                    "sung": [
                        {
                            "id": 2,
                            "title": "car car",
                            "singer": 2,
                            "duration": 4
                        },
                        {
                            "id": 4,
                            "title": "hosa",
                            "singer": 2,
                            "duration": 4
                        }
                    ]
                },
                {
                    "id": 3,
                    "name": "mysore anantswamy",
                    "gender": "male",
                    "sung": [
                        {
                            "id": 3,
                            "title": "yedetumbi",
                            "singer": 3,
                            "duration": 5
                        }
                    ]
                }
            ]
