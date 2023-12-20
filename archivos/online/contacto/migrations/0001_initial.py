# Generated by Django 4.2.7 on 2023-11-05 19:02

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Consulta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nombre", models.CharField(blank=True, max_length=50, null=True)),
                ("descripcion", models.TextField()),
                ("mail", models.EmailField(blank=True, max_length=50, null=True)),
                (
                    "estado_respuesta",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Contestada", "Contestada"),
                            ("No Contestada", "No Contestada"),
                            ("En proceso", "En proceso"),
                        ],
                        default="No Contestada",
                        max_length=15,
                        null=True,
                    ),
                ),
                ("telefono", models.CharField(blank=True, max_length=50, null=True)),
                ("fecha", models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name="Respuesta",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("respuesta", models.TextField()),
                (
                    "fecha",
                    models.DateField(
                        blank=True, default=datetime.datetime.now, editable=False
                    ),
                ),
                (
                    "consulta",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="contacto.consulta",
                    ),
                ),
            ],
        ),
    ]
