from django.shortcuts import render

# Create your views here.


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import FetchedImage
from .serializers import FetchedImageSerializer
import requests
from django.core.files.base import ContentFile
from django.utils.text import slugify

class FetchImageView(APIView):
    def post(self, request, format=None):
        url = request.data.get('url')
        if url:
            response = requests.get(url)
            if response.status_code == 200:
                title = slugify(url.split('/')[-1])
                image = ContentFile(response.content)
                fetched_image = FetchedImage(title=title)
                fetched_image.image.save(title + '.jpg', image)
                fetched_image.save()
                serializer = FetchedImageSerializer(fetched_image)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Failed to fetch the image'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'URL parameter missing'}, status=status.HTTP_400_BAD_REQUEST)


class FetchedImageListView(APIView):
    def get(self):
        fetched_images = FetchedImage.objects.all()
        serializer = FetchedImageSerializer(fetched_images, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
