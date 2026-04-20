from django.db import models
from django.conf import settings

class Conversacion(models.Model):    

    # Vinculamos la conversacion al usuario
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name ='Usuario')
    titulo = models.CharField(max_length=200, default="Nueva conversacion", verbose_name="Titulo de la conversacion")

    # auto_nod_add: se inicializa slo una vez, es decir al crear la conversacion
    # auto_now: se actualiza su valor cada vez que se actualiza la instancia 
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    fecha_actualizacion = models.DateTimeField(auto_now=True, verbose_name="Fecha de actualización")

    class Meta:
        ordering = ['-fecha_actualizacion'] # La más reciente primero
    
    def __str__(self):  
        return f"{self.titulo} - {self.usuario.email}"
    

class Mensaje(models.Model):
    # Los distintos roles que entiende Ollama/Qwen a la hora de pasarle un mensaje
    ROLES = (
        ('user' , 'Usuario'),
        ('assistant', 'AlhambrIA'),
        ('system', 'Sistema'),
    )

    # Vinculamos el mensaje a una conversación
    conversacion = models.ForeignKey(Conversacion,on_delete=models.CASCADE, verbose_name="Conversacion")
    role = models.CharField(max_length=20, choices=ROLES)
    contenido = models.TextField(verbose_name="Contenido del mensaje")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")

    class Meta:
        ordering = ['fecha_creacion'] #En orden cronológico para que el chat se vea bien

    def __str__(self):
        return f"{self.conversacion.titulo} - {self.role} [{self.fecha_creacion.strftime('%H:%M')}]"