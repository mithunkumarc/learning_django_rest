#### readonly fields configured using extra_kwargs attribute


        from rest_framework import serializers
        from .models import Student

        class StudentSerializer(serializers.ModelSerializer):
            class Meta:
                model = Student
                fields = ['name', 'roll', 'city'] # fields = '__all__' # all fields
                extra_kwargs = { 'name': { 'read_only': True} } # name field becomes readonly
