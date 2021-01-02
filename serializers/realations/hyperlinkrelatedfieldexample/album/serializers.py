from .models import Singer, Song
from rest_framework import serializers


class SingerSerializer(serializers.ModelSerializer):
	# instead of song primary key, its hyperlink is shown
	song = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="song-detail")
	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender', 'song']

class SongSerializer(serializers.ModelSerializer):
	# instead of singer primary key, its hyperlink is shown
	singer = serializers.HyperlinkedRelatedField(read_only=True, view_name="singer-detail")
	class Meta:
		model = Song
		fields = ['id', 'title', 'singer', 'duration', 'singer']
