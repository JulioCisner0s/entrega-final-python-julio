# Generated by Django 4.2.11 on 2024-05-23 07:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Format',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Nombre')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('price', models.IntegerField(verbose_name='Precio')),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
                ('image', models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Imagen')),
                ('format', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.format', verbose_name='Formato')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogo.genre', verbose_name='Género')),
            ],
        ),
    ]
