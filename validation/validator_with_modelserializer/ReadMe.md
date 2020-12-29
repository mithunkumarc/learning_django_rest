#### validator function used to validate field and reusable : test in postman


        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.ModelSerializer):
            # validator function
            def is_roll_greater_than_200(value):
                if value >= 200:
                    raise serializers.ValidationError('error : seat full, must be less than 200')

            roll = serializers.CharField(validators=[is_roll_greater_than_200])

            class Meta:
                model = Student
                fields = ['name', 'roll', 'city'] # fields = '__all__' # all fields
