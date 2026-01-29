from django.db import migrations


def seed_proceso_pasos(apps, schema_editor):
    ProcesoCompraPaso = apps.get_model('scompras_app', 'ProcesoCompraPaso')
    Group = apps.get_model('auth', 'Group')

    Group.objects.get_or_create(name='analista')

    pasos_por_tipo = {
        'BAJA_CUANTIA': [
            (1, 'INGRESO SOLICITUD'),
            (2, 'REGISTRO Y REVISIÓN'),
            (3, 'COTIZACIÓN / COMPARATIVO'),
            (4, 'AUTORIZACIÓN DE COMPRA'),
            (5, 'TRÁMITE DE CHEQUE'),
            (6, 'ENTREGA DE CHEQUE'),
            (7, 'ACREDITAMIENTO A CUENTA'),
            (8, 'CONFIRMACIÓN DE PAGO'),
            (9, 'CIERRE DE EXPEDIENTE'),
        ],
        'COMPRA_DIRECTA': [
            (1, 'INGRESO SOLICITUD'),
            (2, 'REGISTRO Y REVISIÓN'),
            (3, 'VALIDACIÓN DE COMPRA DIRECTA'),
            (4, 'EMISIÓN DE ORDEN DE COMPRA'),
            (5, 'RECEPCIÓN DE BIENES/SERVICIOS'),
            (6, 'CIERRE DE EXPEDIENTE'),
        ],
        'COTIZACION': [
            (1, 'INGRESO SOLICITUD'),
            (2, 'REGISTRO Y REVISIÓN'),
            (3, 'SOLICITUD DE COTIZACIONES'),
            (4, 'RECEPCIÓN DE COTIZACIONES'),
            (5, 'EVALUACIÓN Y ADJUDICACIÓN'),
            (6, 'EMISIÓN DE ORDEN DE COMPRA'),
            (7, 'CIERRE DE EXPEDIENTE'),
        ],
        'CONTRATO_ABIERTO': [
            (1, 'INGRESO SOLICITUD'),
            (2, 'REGISTRO Y REVISIÓN'),
            (3, 'ELABORACIÓN DE BASES'),
            (4, 'PUBLICACIÓN Y RECEPCIÓN'),
            (5, 'EVALUACIÓN'),
            (6, 'ADJUDICACIÓN'),
            (7, 'FORMALIZACIÓN DEL CONTRATO'),
            (8, 'CIERRE DE EXPEDIENTE'),
        ],
        'LICITACION': [
            (1, 'INGRESO SOLICITUD'),
            (2, 'REGISTRO Y REVISIÓN'),
            (3, 'ELABORACIÓN DE BASES'),
            (4, 'PUBLICACIÓN'),
            (5, 'RECEPCIÓN DE OFERTAS'),
            (6, 'APERTURA Y EVALUACIÓN'),
            (7, 'ADJUDICACIÓN'),
            (8, 'FORMALIZACIÓN DEL CONTRATO'),
            (9, 'CIERRE DE EXPEDIENTE'),
        ],
    }

    for tipo, pasos in pasos_por_tipo.items():
        for numero, titulo in pasos:
            ProcesoCompraPaso.objects.get_or_create(
                tipo_proceso=tipo,
                numero=numero,
                defaults={
                    'titulo': titulo,
                    'duracion_referencia': '',
                    'activo': True,
                },
            )


def noop_reverse(apps, schema_editor):
    return


class Migration(migrations.Migration):

    dependencies = [
        ('scompras_app', '0025_proceso_compra_pasos'),
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.RunPython(seed_proceso_pasos, noop_reverse),
    ]
