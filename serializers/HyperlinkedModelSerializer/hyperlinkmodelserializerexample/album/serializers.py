from .models import Singer, Song
from rest_framework import serializers

class SingerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Singer
		fields = ['id', 'name', 'gender','url']

class SongSerializer(serializers.HyperlinkedModelSerializer):
	# hyperlink of singer is shown instead of primary key
	singer = serializers.HyperlinkedIdentityField(view_name="song-detail")
	class Meta:
		model = Song
		fields = ['id', 'title', 'singer', 'duration','url']
