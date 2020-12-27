from rest_framework import serializers
from .models import Musician, Album

class MusicianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Musician
        fields = '__all__' # may be requesting to serialize all fields


class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = '__all__' # may be requesting to serialize all fields
