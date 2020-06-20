# Generated by Django 2.2.13 on 2020-06-19 21:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Ventas', '0003_auto_20200619_1651'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subastar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio_subasta', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio a Subastar')),
                ('descripcion', models.TextField(blank=True, null=True, verbose_name='Nota/Descripcion')),
                ('subasta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Ventas.Subasta')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Orden_Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField(default=1)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('venta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Ventas.Venta')),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(blank=True, max_length=20, null=True, verbose_name='Codigo de Referencia')),
                ('fecha_orden', models.DateTimeField(auto_now_add=True)),
                ('productos', models.ManyToManyField(to='Compras.Orden_Compra')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]