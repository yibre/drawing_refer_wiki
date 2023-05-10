from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    fields = ["title", "upper_folder"]