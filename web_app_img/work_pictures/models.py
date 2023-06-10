from django.contrib.auth.models import User
from django.db import models

class PictureSaveVariations(models.Model):
    user = models.ForeignKey(User, verbose_name='Користувач', on_delete=models.CASCADE, blank=True)

    icon = models.ImageField(upload_to="img", blank=False, null=False)
    icon_75 = models.ImageField(upload_to="img", blank=False, null=False)
    icon_50 = models.ImageField(upload_to="img", blank=False, null=False)
    icon_25 = models.ImageField(upload_to="img", blank=False, null=False)

    def __str__(self) -> str:
        return f"{self.user}, {self.id}"