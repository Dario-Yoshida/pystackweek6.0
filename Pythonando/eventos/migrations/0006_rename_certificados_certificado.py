# Generated by Django 4.2 on 2023-04-15 03:11

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eventos', '0005_certificados'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Certificados',
            new_name='Certificado',
        ),
    ]
