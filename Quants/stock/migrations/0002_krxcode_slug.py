# Generated by Django 2.0 on 2017-12-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='krxcode',
            name='slug',
            field=models.SlugField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
