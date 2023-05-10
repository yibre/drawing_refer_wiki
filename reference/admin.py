from django.contrib import admin
from . import models

@admin.register(models.Reference)
class ReferenceAdmin(admin.ModelAdmin):
    fields = ["album", "picture", "uploader"]