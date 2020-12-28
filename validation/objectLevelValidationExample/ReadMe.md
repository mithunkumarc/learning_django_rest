
#### validation done at object level inside serializers.py

#### steps same as https://github.com/mithunkumarc/learning_django_rest/tree/main/validation/fieldvalidationexample

#### the only difference is providing validate(self, incomingObject) in serializers.py

#### school/serializers.py

        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=100)
            roll = serializers.IntegerField()
            city = serializers.CharField(max_length=100)

            # validating roll number
            def validate(self, data):
                if data.get('roll') >= 200:
                    raise serializers.ValidationError('seat full')
                return data

            # for creating student
            def create(self, validated_data):
                return Student.objects.create(**validated_data)


#### test validation error : postman

      post : localhost:8000/studentcreate
      
      {
          "name": "veeresh",
          "roll": 309,
          "city": "davanagere"
      }
      
      response : 
      {
          "non_field_errors": [
              "seat full"
          ]
      }
