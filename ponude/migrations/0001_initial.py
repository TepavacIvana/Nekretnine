# Generated by Django 3.2.9 on 2021-11-24 16:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('kupci', '0001_initial'),
        ('stanovi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ponuda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_or_company_name', models.CharField(blank=True, max_length=80, null=True)),
                ('citizen', models.BooleanField(default=True)),
                ('company', models.BooleanField(default=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_num', models.CharField(max_length=50)),
                ('PIB_JMBG', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('offer_date', models.DateTimeField(auto_now_add=True)),
                ('potential', models.BooleanField(default=True)),
                ('reserved', models.BooleanField(default=False)),
                ('bought', models.BooleanField(default=False)),
                ('price_for_buyer', models.IntegerField()),
                ('note', models.TextField(blank=True)),
                ('contract_num', models.CharField(max_length=50)),
                ('contract_date', models.DateTimeField(auto_now_add=True)),
                ('prodaja_detail', models.CharField(choices=[('cela_suma', 'Cela suma'), ('kredit', 'Kredit'), ('rate', 'Rate'), ('ucesce', 'Ucesce')], default='cela_suma', max_length=50)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ponude', to='stanovi.stan')),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ponude', to='kupci.kupac')),
            ],
        ),
    ]