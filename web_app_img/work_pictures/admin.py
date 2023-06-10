from django.contrib import admin
from .models import PictureSaveVariations

class IconFormatAdmin(admin.ModelAdmin):
    list_display = ('user', 'id')
    search_fields = ('user', 'id')

admin.site.register(PictureSaveVariations, IconFormatAdmin)
