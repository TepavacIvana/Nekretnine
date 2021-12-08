from datetime import date

from django.db import models

from korisnici.models import Korisnik
from kupci.models import Kupac
from stanovi.models import Stan


class Ponuda(models.Model):
    class ProdajaDetail(models.TextChoices):
        FULL_PRICE = 'full_price', "Full Price"
        CREDIT = 'credit', "Credit"
        INSTALLMENT = 'installment', "Installment"
        PARTICIPATION = 'participation', "Participation"

    class SalesStatus(models.TextChoices):
        POTENTIAL = 'potential', "Potential"
        RESERVED = 'reserved', "Reserved"
        BOUGHT = 'bought', "Bought"

    id_ponude = models.BigAutoField(db_column='id_ponude', primary_key=True)
    apartment = models.ForeignKey(Stan, on_delete=models.CASCADE, db_column='id_stana',
                                  related_name='lista_ponuda_stana')
    buyer = models.ForeignKey(Kupac, on_delete=models.CASCADE, db_column='id_kupca',
                              related_name='lista_ponuda_kupca')
    finance = models.ForeignKey(Korisnik, related_name='ponude', on_delete=models.CASCADE, default=1)
    sales_status = models.CharField(max_length=50, choices=SalesStatus.choices, default=SalesStatus.POTENTIAL)
    price_for_buyer = models.IntegerField()
    note = models.TextField(blank=True)
    contract_num = models.CharField(max_length=50, unique=True)
    contract_date = models.DateField(default=date.today)
    prodaja_detail = models.CharField(max_length=50, choices=ProdajaDetail.choices, default=ProdajaDetail.FULL_PRICE)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.buyer.id_kupca}, {self.buyer.full_or_company_name}, {self.apartment.id_stana}" \
               f" - {self.contract_num}, {self.price_for_buyer}"
