from django.db import models


class File(models.Model):
    file = models.FileField(upload_to='upload')
    date_upload = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_upload',)


class BrandData(models.Model):
    article = models.IntegerField()
    brand = models.CharField(max_length=100)
    title = models.CharField(max_length=255)
    datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'brand_data'