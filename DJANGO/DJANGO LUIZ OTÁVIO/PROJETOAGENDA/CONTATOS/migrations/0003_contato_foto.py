# Generated by Django 4.0.1 on 2022-01-25 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CONTATOS', '0002_contato_mostrar'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foto',
            field=models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d'),
        ),
    ]
