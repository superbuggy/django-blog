# Generated by Django 2.0.4 on 2018-04-25 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scribble', '0005_song'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='preview_url',
            field=models.TextField(default=''),
        ),
    ]