# Generated by Django 3.2.9 on 2021-11-30 15:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('clothes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saved',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saved', models.BooleanField(default=False)),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved', to='clothes.clothes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='saved_c', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('like', models.BooleanField(default=False)),
                ('review', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', to='clothes.clothes')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_like', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]