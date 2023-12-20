from django.db import models
from django.core.mail import send_mail
from django.utils.html import format_html
from datetime import datetime
from django.core.mail import send_mail


class Consulta(models.Model):

    CONTESTADA = "Contestada"
    NOCONTESTADA = "No Contestada"
    ENPROCESO = "En proceso"
    ESTADOS = (
        (CONTESTADA, "Contestada"),
        (NOCONTESTADA, "No Contestada"),
        (ENPROCESO, "En proceso"),
    )

    nombre = models.CharField(max_length=50, blank=True, null=True)
    descripcion = models.TextField(blank=False, null=False)
    mail = models.EmailField(max_length=50, blank=True, null=True)
    estado_respuesta = models.CharField(
        max_length=15, blank=True, null=True, choices=ESTADOS, default=NOCONTESTADA
    )
    telefono = models.CharField(max_length=50, blank=True, null=True)
    fecha = models.DateField(default=datetime.now, blank=True, editable=True)

    def __str__(
        self,
    ):
        return self.nombre

    def estado_de_respuesta(
        self,
    ):
        if self.estado_respuesta == "Contestada":
            return format_html(
                '<spam style="background-color:#0a0; color:#fff; padding:5px;">{}</spam>',
                self.estado_respuesta,
            )
        elif self.estado_respuesta == "No Contestada":
            return format_html(
                '<spam style="background-color:#a00; color:#fff; padding:5px;">{}</spam>',
                self.estado_respuesta,
            )
        elif self.estado_respuesta == "En proceso":
            return format_html(
                '<spam style="background-color:#FFFF00; color:#000; padding:5px;">{}</spam>',
                self.estado_respuesta,
            )


class Respuesta(models.Model):

    consulta = models.ForeignKey(
        Consulta, blank=False, null=True, on_delete=models.CASCADE
    )
    respuesta = models.TextField()
    fecha = models.DateField(default=datetime.now, blank=True, editable=False)
    # history = HistoricalRecords()

    def create_mensaje(self):

        consulta_cambio_estado = Consulta.objects.get(id=self.consulta.id)
        consulta_cambio_estado.estado_respuesta = "Contestada"
        consulta_cambio_estado.save()

    # poner logica para enviar email

    def save(self, *args, **kwargs):
        self.create_mensaje()
        force_update = False
        if self.id:
            force_update = True
        super(Respuesta, self).save(force_update=force_update)
