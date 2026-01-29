from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scompras_app', '0024_constanciadisponibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudcompra',
            name='analista_asignado',
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name='solicitudes_asignadas',
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name='solicitudcompra',
            name='tipo_proceso',
            field=models.CharField(
                choices=[
                    ('BAJA_CUANTIA', 'Baja cuantía'),
                    ('COMPRA_DIRECTA', 'Compra directa'),
                    ('COTIZACION', 'Cotización'),
                    ('CONTRATO_ABIERTO', 'Contrato abierto'),
                    ('LICITACION', 'Licitación'),
                ],
                default='COMPRA_DIRECTA',
                max_length=30,
            ),
        ),
        migrations.AddField(
            model_name='solicitudcompra',
            name='subtipo_baja_cuantia',
            field=models.CharField(
                blank=True,
                choices=[
                    ('CHEQUE', 'Trámite de cheque'),
                    ('ACREDITAMIENTO', 'Acreditamiento a cuenta'),
                ],
                max_length=20,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name='solicitudcompra',
            name='paso_actual',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='solicitudcompra',
            name='fecha_asignacion_analista',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='ProcesoCompraPaso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_proceso', models.CharField(choices=[
                    ('BAJA_CUANTIA', 'Baja cuantía'),
                    ('COMPRA_DIRECTA', 'Compra directa'),
                    ('COTIZACION', 'Cotización'),
                    ('CONTRATO_ABIERTO', 'Contrato abierto'),
                    ('LICITACION', 'Licitación'),
                ], max_length=30)),
                ('numero', models.PositiveIntegerField()),
                ('titulo', models.CharField(max_length=255)),
                ('duracion_referencia', models.CharField(blank=True, max_length=80)),
                ('activo', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['tipo_proceso', 'numero'],
                'unique_together': {('tipo_proceso', 'numero')},
            },
        ),
        migrations.CreateModel(
            name='SolicitudPasoEstado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completado', models.BooleanField(default=False)),
                ('fecha_completado', models.DateTimeField(blank=True, null=True)),
                ('nota', models.TextField(blank=True)),
                ('completado_por', models.ForeignKey(
                    blank=True,
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to=settings.AUTH_USER_MODEL,
                )),
                ('paso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scompras_app.procesocomprapaso')),
                ('solicitud', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pasos_estado', to='scompras_app.solicitudcompra')),
            ],
            options={
                'unique_together': {('solicitud', 'paso')},
            },
        ),
    ]
