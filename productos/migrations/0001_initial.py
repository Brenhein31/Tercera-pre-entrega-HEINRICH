from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('nombre_autor', models.CharField(max_length=256)),
                ('apellido_autor', models.CharField(max_length=256)),
                ('ISBN', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Musica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=256)),
                ('nombre_autor', models.CharField(max_length=256)),
                ('genero', models.CharField(max_length=256)),
            ],
        ),
    ]
