#### ModelSerializer : 

1. provides shortcut that lets you to create a serializer class with fields corresponds to Model fields.
2. automatically generates set of fields for you, based on model. No need to create fields again(like if you use regular Serializer)
3. automatically generate validators such as unique_together_validators
4. default implementations of create() and update()

syntax : 

      class StudentSerializer(serialzers.ModelSerializer):
            class Meta:
                  model = Student         # import Student model
                  fields = '__all__'      # use __all__ insteat of ['id', 'name', 'city' ], you can exclude too

#### serializers.Serializer vs serializers.ModelSerializer

1. serializers.Serializer : we have to provide crud methods

      need to provide create(), update, delete methods 
    
2. serializers.ModelSerialzer

      class StudentSerializer(serializers.ModelSerializer):

          ...fields here

          class Meta:
              model = Student #import student model
              fields = '__all__'  # covers crud methods

