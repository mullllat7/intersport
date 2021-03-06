# Generated by Django 3.2.9 on 2021-11-29 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('brand', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Clothes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_of_clothes', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=11)),
                ('in_stock', models.BooleanField(default=True)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='clothes', to='brand.brand')),
            ],
        ),
        migrations.CreateModel(
            name='ClothesImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('clothes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='clothes.clothes')),
            ],
        ),
    ]
