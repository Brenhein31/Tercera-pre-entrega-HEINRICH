# Generated by Django 4.2.3 on 2023-07-30 00:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libros',
            name='ISBN',
            field=models.IntegerField(),
        ),
    ]