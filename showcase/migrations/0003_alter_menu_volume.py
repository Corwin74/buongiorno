# Generated by Django 4.0.5 on 2022-06-29 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0002_menu_volume'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='volume',
            field=models.IntegerField(default=250),
        ),
    ]
