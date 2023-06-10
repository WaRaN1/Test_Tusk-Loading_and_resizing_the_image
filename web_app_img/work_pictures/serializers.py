from .models import PictureSaveVariations
from rest_framework import serializers

class ImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = PictureSaveVariations
        fields = ['user', 'icon']