# Generated by Django 3.2.4 on 2021-07-01 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]