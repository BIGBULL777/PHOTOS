from rest_framework import serializers
from .models import *

class FetchedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = FetchedImage
        fields = '__all__'
