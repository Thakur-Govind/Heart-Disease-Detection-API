from django.db import models

# Create your models here.
class MlModel(models.Model):
    name = models.CharField(max_length=1000)
    params = models.TextField()
    model = models.FileField(upload_to='uploads/')
    