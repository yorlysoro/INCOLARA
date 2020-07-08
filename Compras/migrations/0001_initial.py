# Generated by Django 2.2.13 on 2020-07-08 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ventas', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subastar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_subasta', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio a Subastar')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Nota/Descripcion')),
                ('subasta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ventas.Subasta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cuenta_Subastar', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Subastar',
                'verbose_name_plural': 'Subastar',
            },
        ),
        migrations.CreateModel(
            name='Orden_Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cuenta_Orden_Compra', to=settings.AUTH_USER_MODEL)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ventas.Venta')),
            ],
            options={
                'verbose_name': 'Orden de Compra',
                'verbose_name_plural': 'Ordenes de Compra',
            },
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Codigo de Referencia')),
                ('fecha_orden', models.DateTimeField(auto_now_add=True)),
                ('productos', models.ManyToManyField(to='Compras.Orden_Compra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Cuenta_Orden', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Orden',
                'verbose_name_plural': 'Ordenes',
            },
        ),
    ]
