# Generated by Django 3.2.9 on 2021-11-24 15:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kupci', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Stan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advertised', models.DateTimeField(auto_now_add=True)),
                ('district', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('lamella', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('floor', models.IntegerField()),
                ('num_of_rooms', models.FloatField()),
                ('orientation', models.CharField(max_length=30)),
                ('num_of_terraces', models.IntegerField()),
                ('price', models.IntegerField()),
                ('available', models.BooleanField(default=True)),
                ('reserved', models.BooleanField(default=False)),
                ('sold', models.BooleanField(default=False)),
                ('image', models.ImageField(default='static/images/stan.jpg', upload_to='static/images/')),
                ('buyer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='stanovi', to='kupci.kupac')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stanovi', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['price'],
            },
        ),
    ]
