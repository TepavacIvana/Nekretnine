from datetime import date

from django.db import models

from korisnici.models import Korisnik


class Stan(models.Model):
    # class StatusApt(models.TextChoices):
    #     AVAILABLE = 'Available', "Available"
    #     RESERVED = 'Reserved', "Reserved"
    #     SOLD = 'sold', "Sold"

    id_stana = models.BigAutoField(db_column='id_stana', primary_key=True)
    advertised = models.DateField(default=date.today)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    lamella = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    floor = models.IntegerField()
    num_of_rooms = models.FloatField()
    orientation = models.CharField(max_length=30)
    num_of_terraces = models.IntegerField()
    price = models.IntegerField()
    # status_apt = models.CharField(max_length=50, choices=StatusApt.choices, default=StatusApt.AVAILABLE)
    available = models.BooleanField(default=True)
    image = models.ImageField(upload_to='static/images/', default='static/images/stan.jpg')
    """ owner = prodavac """
    owner = models.ForeignKey(Korisnik, related_name='stanovi', on_delete=models.CASCADE)

    class Meta:
        # ordering = ['-advertised']
        # ordering = ['price']            # ascending
        # ordering = ['-price']           # descending
        ordering = ['-id_stana']

    def __str__(self):
        return f"{self.id_stana}, {self.address}"

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
