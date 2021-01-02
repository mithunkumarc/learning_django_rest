from .models import Singer, Song
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
	# make sure you have overridden Song class __str__ method
	song = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender', 'song']

class SongSerializer(serializers.ModelSerializer):
	# make sure you have overridden Singer class __str__ method
	singer = serializers.StringRelatedField(read_only=True)
	class Meta:
		model = Song
		fields = ['id', 'title', 'singer', 'duration', 'singer']
