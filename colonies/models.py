from django.db import models

class Colony(models.Model):
    name = models.CharField(max_length=32, verbose_name='Nombre', null=True, blank=True)
    link_gmap = models.URLField(verbose_name='Link Google Maps', null=True, blank=True)
    # image_landscape = models.ImageField(upload_to='colony-landscape', verbose_name='Foto del lugar', blank=True, null=True)
    # localization
    # long - lat ?
    # district

    def __str__(self):
        return self.name