# Generated by Django 2.0.1 on 2018-01-30 16:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='release_date',
        ),
    ]