# Generated by Django 2.2.14 on 2020-07-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Base', '0002_auto_20200713_1056'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cuenta',
            name='sector',
        ),
        migrations.AddField(
            model_name='cuenta',
            name='sector',
            field=models.ManyToManyField(to='Base.Sectores'),
        ),
    ]