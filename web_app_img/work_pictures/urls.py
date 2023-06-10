from django.urls import path
from .views import DownloadImageView

urlpatterns = [
    path('', DownloadImageView.as_view(), name='upload_image'),
]