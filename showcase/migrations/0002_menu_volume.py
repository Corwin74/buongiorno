# Generated by Django 4.0.5 on 2022-06-29 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='volume',
            field=models.ImageField(default=250, upload_to=''),
        ),
    ]
