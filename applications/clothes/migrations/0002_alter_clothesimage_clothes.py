# Generated by Django 3.2.9 on 2021-11-26 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothesimage',
            name='clothes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='clothes.clothes'),
        ),
    ]
