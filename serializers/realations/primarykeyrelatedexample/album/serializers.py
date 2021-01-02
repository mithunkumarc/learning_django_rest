from .models import Singer, Song
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
	# song field shows primary key id
	song = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender', 'song']

class SongSerializer(serializers.ModelSerializer):
	# singer field shows primary key id
	singer = serializers.PrimaryKeyRelatedField(read_only=True)
	class Meta:
		model = Song
		fields = ['id', 'title', 'singer', 'duration', 'singer']
