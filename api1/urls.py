from django.urls import path
from . import views

urlpatterns = [
    path('api/fetch/', views.FetchImageView.as_view(), name='fetch_image_api'),
    path('api/images/', views.FetchedImageListView.as_view(), name='fetched_image_list_api'),
]
