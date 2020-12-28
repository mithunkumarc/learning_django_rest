from rest_framework import serializers

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    roll = serializers.IntegerField()
    city = serializers.CharField(max_length=100)

    def validate_roll(self, value):
        if value >= 200:
            raise serializers.ValidationError('seat full')
        return value
