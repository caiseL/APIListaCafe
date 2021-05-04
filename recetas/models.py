from django.db import models
from slugify import slugify


def image_path(instance, filename):
    # Nombre para el archivo que se va a crear
    ext = filename.split('.')[-1]
    return "recetas/{0}.{1}".format(slugify(instance.nombre), ext)


class Receta(models.Model):
    nombre = models.CharField(max_length=50)
    campo_receta = models.CharField(max_length=500)
    numero_personas = models.PositiveIntegerField()
    imagen = models.ImageField(upload_to=image_path)

    def __str__(self):
        return f"{self.nombre} para {self.personas} personas"
