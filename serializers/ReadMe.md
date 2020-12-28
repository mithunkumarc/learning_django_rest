#### serializers.Serializer vs serializers.ModelSerializer

1. serializers.Serializer : we have to provide crud methods

      need to provide create(), update, delete methods 
    
2. serializers.ModelSerialzer

      class StudentSerializer(serializers.ModelSerializer):

          ...fields here

          class Meta:
              model = Student #import student model
              fields = '__all__'  # covers crud methods
