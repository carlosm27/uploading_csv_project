from django.db import models
from django.conf import settings
# Create your models here.

class Document(models.Model):
    description = models.CharField(max_length = 255, blank = True)
    document = models.FileField(upload_to = 'documents/')
    uploaded_at = models.DateTimeField(auto_now_add = True)
    path = models.FilePathField(path=settings.MEDIA_ROOT, default=settings.MEDIA_ROOT)

    def __str__(self):
        return self.document