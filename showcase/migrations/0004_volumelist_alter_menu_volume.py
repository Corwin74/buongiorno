# Generated by Django 4.0.5 on 2022-06-29 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('showcase', '0003_alter_menu_volume'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolumeList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='menu',
            name='volume',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='showcase.volumelist'),
        ),
    ]
