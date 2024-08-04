from colonies.models import Colony
from diseases.models import Disease
from django.db import models
from cats import utils
import pdb
import os

T_SEX_CHOICES = ((False, 'Macho'), (True, 'Hembra'))
T_STATE_CHOICES = ((0, 'Presente'), (1, 'Fallecido'),(2, 'Desaparecido'),(3,'Adoptado'))
T_YES_NO = ((False,'No'),(True,'Sí'))
T_FREQUENCY = ((0,'Habitual'),(1,'Ocasional'))
T_SOCIABILITY = ((0,'Sí'),(1,'Ocasional'),(2,'No'))

class Cat(models.Model):
    photo = models.ImageField(upload_to='cat-photos', verbose_name='Icono', blank=True, null=True)
    thumbnail = models.ImageField(upload_to='cat-thumbnails', verbose_name='Icono', blank=True, null=True)
    
    name = models.CharField(max_length=32, blank=True, null=True, verbose_name='Nombre')
    colony = models.ForeignKey(to=Colony, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Colonia')
    gender = models.BooleanField(choices=T_SEX_CHOICES, blank=True, null=True, verbose_name='Sexo')
    # sterilized = models.BooleanField(choices=T_YES_NO, blank=True, null=True, verbose_name='Esterilizado')
    sterilized = models.BooleanField(blank=False, default=False, verbose_name='Esterilizado')
    
    # Advanced Options
    sterlize_date = models.DateField(blank=True, null=True, verbose_name='Fecha de esterilización')
    state = models.PositiveSmallIntegerField(blank=True, null=True, choices=T_STATE_CHOICES, default=0, verbose_name='Estado')
    frequency = models.PositiveSmallIntegerField(blank=True, null=True, choices=T_FREQUENCY, verbose_name='Frecuencia de visita', default=0)
    sociability = models.PositiveSmallIntegerField(blank=True, null=True, choices=T_SOCIABILITY, verbose_name='Sociable', default=1)
    sighting_date = models.DateField(verbose_name='Fecha de avistamiento', blank=True, null=True)
    disease = models.ForeignKey(to=Disease, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Afecciones')
    
    record_date = models.DateField(auto_now=True, verbose_name='Fecha de registro', blank=True, null=True)
    pictures = models.ManyToManyField(to='CatPicture', related_name='cats', blank=True)
    # tray_picture = models.ForeignKey(to='CatPicture', related_name='tray_for_cat', on_delete=models.SET_NULL, null=True, blank=True)

    def delete(self, *args, **kwargs):
        for picture in self.pictures.all():
            picture.delete(save=False)

        if self.photo and os.path.isfile(self.photo.path):
            self.photo.delete(save=False)
        
        # pdb.set_trace()

        if self.thumbnail and os.path.isfile(self.thumbnail.path):
            self.thumbnail.delete(save=False)

        super().delete(*args, **kwargs)


    def save(self, *args, **kwargs):
    
        if self.id:
            cat = Cat.objects.get(id=self.id)
            if cat.photo and os.path.isfile(cat.photo.path):
                cat.photo.delete(save=False)
            if cat.thumbnail and os.path.isfile(cat.thumbnail.path):
                cat.thumbnail.delete(save=False)
        else:
            super().save(*args, **kwargs)

        bytes_io = utils.to_thumbnail(self.photo)
        file_name = utils.format_image_name(self.id)
        self.thumbnail.save(name=file_name, content=bytes_io, save=False)

        super().save(*args, **kwargs)

class CatPicture(models.Model):
    image = models.ImageField(upload_to='cats', verbose_name='Foto')
    date = models.DateField(verbose_name='Fecha', blank=True, null=True)

    def delete(self, *args, **kwargs):
        self.image.delete()  # This deletes the real image aswell
        super(CatPicture, self).delete(*args, **kwargs)