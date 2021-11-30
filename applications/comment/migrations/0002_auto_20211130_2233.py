# Generated by Django 3.2.9 on 2021-11-30 16:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clothes', '0004_auto_20211130_2233'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='review',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='like',
            old_name='review',
            new_name='comment',
        ),
        migrations.AlterField(
            model_name='comment',
            name='clothes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment', to='clothes.clothes'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comment', to=settings.AUTH_USER_MODEL),
        ),
    ]
