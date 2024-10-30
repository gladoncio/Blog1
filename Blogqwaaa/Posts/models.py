from django.db import models
import uuid
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_delete
from django.db.models.signals import pre_delete,post_migrate
import logging
from django.dispatch import receiver
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, null=True, blank= True)
    description = RichTextUploadingField(null=True, blank= True)
    imagen_portada = models.ImageField(null=True, blank=True, default = "default-image.png")
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title
    
    

logger = logging.getLogger(__name__)

class Usuario(AbstractUser):
    foto_perfil = models.ImageField(upload_to='fotos_perfil/', null=True, blank=True)

# Define la función para crear el usuario admin
def crear_usuario_admin(**kwargs):
    if not Usuario.objects.filter(username='admin').exists():
        Usuario.objects.create_superuser(username='admin', password='123')
        print("Usuario administrador creado exitosamente.")
# Registra la función con la señal post_migrate
@receiver(post_migrate)
def post_migrate_callback(sender, **kwargs):
    crear_usuario_admin(**kwargs)
