# Generated by Django 3.2.4 on 2021-07-05 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0004_alter_instrument_artist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instrument',
            name='track',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='feed.track'),
        ),
    ]