#### use postman to test

#### follw steps of fieldlevelvalidaiton

#### rootproject/school/serializers.py

        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Student
                fields = ['name', 'roll', 'city'] # fields = '__all__' # all fields

            def validate_roll(self, value):
                if value >= 200:
                    raise serializers.ValidationError('error : seat full, must be less than 200')
                return value
