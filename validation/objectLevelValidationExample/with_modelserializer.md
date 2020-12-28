serializer.py inherting modelserializer 

        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.ModelSerializer):
            # no need to declare fields here
            class Meta:
                model = Student
                fields = '__all__'

            # validating roll number field
            def validate(self, data):
                if data.get('roll') >= 200:
                    raise serializers.ValidationError('error : seat full, must be less than 200')
                return data
