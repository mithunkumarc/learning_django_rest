from .models import Singer, Song
from rest_framework import serializers

class SingerSerializer(serializers.ModelSerializer):
	# hyperlink of song is shown instead of primary key
	song = serializers.HyperlinkedIdentityField(view_name="singer-detail")
	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender', 'song']

class SongSerializer(serializers.ModelSerializer):
	# hyperlink of singer is shown instead of primary key
	singer = serializers.HyperlinkedIdentityField(view_name="song-detail")
	class Meta:
		model = Song
		fields = ['id', 'title', 'singer', 'duration', 'singer']
