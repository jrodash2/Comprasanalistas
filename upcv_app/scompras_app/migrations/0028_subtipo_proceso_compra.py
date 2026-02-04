from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scompras_app', '0027_tipoprocesocompra_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SubtipoProcesoCompra',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('codigo', models.SlugField(max_length=40)),
                ('activo', models.BooleanField(default=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subtipos', to='scompras_app.tipoprocesocompra')),
            ],
            options={
                'ordering': ['tipo', 'nombre'],
                'unique_together': {('tipo', 'codigo')},
            },
        ),
    ]
