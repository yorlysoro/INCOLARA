# Generated by Django 2.2.13 on 2020-07-08 18:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Inventario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Venta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio')),
                ('nota', models.TextField(blank=True, null=True, verbose_name='Nota/Descripcion')),
                ('fecha_publicacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Publicacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('info_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Producto')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Venta_Cuenta', to=settings.AUTH_USER_MODEL)),
                ('variante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Variante')),
            ],
            options={
                'verbose_name': 'Venta',
                'verbose_name_plural': 'Ventas',
            },
        ),
        migrations.CreateModel(
            name='Subasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=255, verbose_name='Titulo')),
                ('precio', models.DecimalField(decimal_places=2, default=0.0, max_digits=10, verbose_name='Precio')),
                ('nota', models.TextField(blank=True, null=True, verbose_name='Nota/Descripcion')),
                ('fecha_publicacion', models.DateField(auto_now_add=True, verbose_name='Fecha de Publicacion')),
                ('fecha_modificacion', models.DateField(auto_now=True, verbose_name='Fecha de Modificacion')),
                ('inicio', models.DateField(verbose_name='Fecha de Apertura')),
                ('final', models.DateField(verbose_name='Fecha de Culminacion')),
                ('info_producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Producto')),
                ('usuario', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='Subasta_Cuenta', to=settings.AUTH_USER_MODEL)),
                ('variante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Inventario.Variante')),
            ],
            options={
                'verbose_name': 'Subasta',
                'verbose_name_plural': 'Subastas',
            },
        ),
    ]
