from django.db import models
from django.contrib.auth.models import AbstractUser


class Korisnik(AbstractUser):

    class KorisnikPristup(models.TextChoices):
        ADMINISTRATOR = 'Administrator', 'Administrator'
        PRODAVAC = 'Prodavac', 'Prodavac'
        FINANSIJE = 'Finansije', 'Finansije'

    first_name = models.CharField('First name', max_length=30, blank=True, null=True)
    last_name = models.CharField('Last name', max_length=50, blank=True, null=True)
    role = models.CharField('Role', max_length=50, choices=KorisnikPristup.choices,
                            default=KorisnikPristup.ADMINISTRATOR, blank=False, null=False)
    email = models.EmailField('Email', unique=True)
    username = models.CharField('Username', unique=True, max_length=50, blank=False, null=False)
    password = models.CharField('Password', max_length=100, blank=False, null=False)
    password2 = models.CharField('Password2', max_length=100, blank=False, null=False, default='')

    def __str__(self):
        return f"{self.username} - {self.first_name} {self.last_name}"
