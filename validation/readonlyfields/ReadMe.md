#### readonly fields : use admin UI : if you try to give new value, no error but values cannot be changed

#### root project / school app / serializers.py

        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Student
                fields = '__all__'
                read_only_fields = ['name', 'roll']  # name and roll fields read only

            def validate(self, data):
                if data.get('roll') >= 200:
                    raise serializers.ValidationError('error : seat full, must be less than 200')
                return data
