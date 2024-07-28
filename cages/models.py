from django.db import models


class Cage(models.Model):
    width = models.PositiveSmallIntegerField(blank=True, null=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True)
    length = models.PositiveSmallIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='cages')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Cage, self).delete(*args, **kwargs)
