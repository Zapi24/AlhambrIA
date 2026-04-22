from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


# Para que DJango cree usuarios sin el campo "username"
class UsuarioManager(BaseUserManager):

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('El email es obligatorio.')
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)


# EL modelo de usuario
class Usuario(AbstractUser):

    # Eliminamos el username por defecto ya que vamos a utilizar el email
    username = None

    email = models.EmailField(unique=True, verbose_name="Correo electrónico")
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    apellidos = models.CharField(max_length=100, verbose_name="Apellidos")
    telefono = models.CharField(max_length=9, blank=True, null=True, verbose_name="Nº de teléfono")
    puesto = models.CharField(max_length=100, blank=True, null=True, verbose_name="Puesto")
    foto_perfil = models.ImageField(upload_to='perfiles/',blank=True, null=True, verbose_name="Foto de perfil")

    objects = UsuarioManager()

    # Hay que decirle a Dkango que el emal es el id principal para el login
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ["nombre", "apellidos"]

    def __str__(self):
        return f"{self.nombre} {self.apellidos} ({self.email})"