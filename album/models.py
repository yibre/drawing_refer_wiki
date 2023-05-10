from django.db import models
from core.models import TimeStampedModel

# Create your models here.
class Album(TimeStampedModel):
    maker = models.ForeignKey("user.User", null=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=100)
    upper_folder = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.title}"