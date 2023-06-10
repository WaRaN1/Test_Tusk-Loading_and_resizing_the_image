from .models import PictureSaveVariations
from rest_framework import serializers

class ImageSerializers(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = PictureSaveVariations
        fields = ['user', 'icon']
