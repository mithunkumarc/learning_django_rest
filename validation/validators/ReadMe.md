#### validators are reusable functions , can be used to validate field inside serializers.py file

#### steps



#### school/serialzers.py

        from rest_framework import serializers
        from .models import Student


        # validator function
        def is_roll_number_greaterthan_200(value):
            if value > 200:
                raise serializers.ValidationError('seat full, must be less than 200')

        class StudentSerializer(serializers.Serializer):
            name = serializers.CharField(max_length=100)
            roll = serializers.IntegerField(validators=[is_roll_number_greaterthan_200])
            city = serializers.CharField(max_length=100)

            # for creating student
            def create(self, validated_data):
                return Student.objects.create(**validated_data)


#### testing : postman : admin UI may not raise validator error 

        post : localhost:8000/studentcreate
        {
            "name": "veeresh",
            "roll": 309,
            "city": "davanagere"
        }

        error : 
        {
            "roll": [
                "seat full, must be less than 200"
            ]
        }
