# Generated by Django 5.1.6 on 2025-04-11 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profil', '0012_rename_qabul_xabar_receiver'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Xabar',
            new_name='Chat',
        ),
    ]
