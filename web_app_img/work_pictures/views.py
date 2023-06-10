from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import ImgForm
from .models import PictureSaveVariations
from django.http import HttpResponseNotFound, HttpResponse

from .serializers import ImageSerializers
from .tasks import optimize_image_with_quality_levels

class UploadImageView(APIView):
    def post(self, request):
        serializer = ImageSerializers(data=request.data)

        if serializer.is_valid():
            image = serializer.save(user=request.user)
            image_id = image.pk
            optimize_image_with_quality_levels.delay(image.pk)

        return Response({
                'message': 'Image uploaded and sent for optimization. Choose your quality in the URL when it`s will be done.',
                'file_100_url': f'http://127.0.0.1:8000/download-image/?id={image_id}&quality=100',
                'file_75_url': f'http://127.0.0.1:8000/download-image/?id={image_id}&quality=75',
                'file_50_url': f'http://127.0.0.1:8000/download-image/?id={image_id}&quality=50',
                'file_25_url': f'http://127.0.0.1:8000/download-image/?id={image_id}&quality=25',
            })



class DownloadImageView(APIView):
    def get(self, request) -> HttpResponse:
        if not request.GET.get('id'):
            form = ImgForm()
            return render(request, 'main_page.html', {'form': form})

        image_id = request.GET.get('id')
        quality = request.GET.get('quality')
        icon_format_instance = PictureSaveVariations.objects.get(id=image_id)

        image_data = self._get_image_file_content_by_quality(request, icon_format_instance, quality)

        if isinstance(image_data, HttpResponseNotFound):
            return image_data

        response = HttpResponse(image_data, content_type='image/jpeg')
        response['Content-Disposition'] = 'attachment; filename="image.jpg"'
        return response

    def _get_image_file_content_by_quality(self, request, icon_format_instance, quality) -> HttpResponseNotFound | bytes:
        quality_to_icon = {
            100: icon_format_instance.icon,
            75: icon_format_instance.icon_75,
            50: icon_format_instance.icon_50,
            25: icon_format_instance.icon_25
        }

        icon = quality_to_icon.get(int(quality))
        if not icon:
            return HttpResponseNotFound()

        with open(icon.path, 'rb') as f:
            image_data = f.read()
            return image_data
