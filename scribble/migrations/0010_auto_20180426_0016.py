# Generated by Django 2.0.4 on 2018-04-26 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scribble', '0009_auto_20180426_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artist',
            name='photo_url',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='song',
            name='preview_url',
            field=models.TextField(default=''),
        ),
    ]
