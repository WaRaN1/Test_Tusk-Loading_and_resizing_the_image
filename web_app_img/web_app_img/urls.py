from django.contrib import admin
from django.urls import path, include
from work_pictures.views import DownloadImageView, UploadImageView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('work_pictures.urls')),

    path('image/<int:user_id>/<int:quality>/', UploadImageView.as_view(), name='image-download'),
    path('download-image/', DownloadImageView.as_view(), name='download_image'),
    path('upload-image/', UploadImageView.as_view(), name='upload_image')
]
