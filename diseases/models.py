from django.db import models

class Disease(models.Model):
    name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
