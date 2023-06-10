from __future__ import absolute_import, unicode_literals
from celery import shared_task
from .models import PictureSaveVariations
from .services import ImageOptimizer



@shared_task
def optimize_image_with_quality_levels(image_id):
    format_instance  = PictureSaveVariations.objects.get(id=image_id)

    quality_levels = [0.25, 0.50, 0.75]
    for quality in quality_levels:
        image_optimizer = ImageOptimizer(format_instance,quality)
        resized_img = image_optimizer.resize_img()
        image_optimizer.save_resized_image(resized_img)

