from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='upload')
    date_upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_upload',)
