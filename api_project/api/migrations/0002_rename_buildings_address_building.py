# Generated by Django 4.0.4 on 2022-05-08 19:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='buildings',
            new_name='building',
        ),
    ]