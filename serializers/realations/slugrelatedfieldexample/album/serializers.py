from .models import Singer, Song
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
	# instead of showing primary key, title of song is shown	
	song = serializers.SlugRelatedField(many=True, read_only=True, slug_field="title")
	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender', 'song']

class SongSerializer(serializers.ModelSerializer):
	# instead of showing primary key, name of singer shown
	singer = serializers.SlugRelatedField(read_only=True, slug_field="name")
	class Meta:
		model = Song
		fields = ['id', 'title', 'singer', 'duration', 'singer']
