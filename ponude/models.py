from django.db import models


class Ponuda(models.Model):

    class ProdajaDetail(models.TextChoices):
        U_CELOSTI = 'cela_suma', "Cela suma"
        KREDIT = 'kredit', "Kredit"
        RATE = 'rate', "Rate"
        UCESCE = 'ucesce', "Ucesce"

    full_or_company_name = models.CharField(max_length=80, blank=True, null=True)
    citizen = models.BooleanField(default=True)
    company = models.BooleanField(default=False)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=50)
    PIB_JMBG = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    offer_date = models.DateTimeField(auto_now_add=True)
    potential = models.BooleanField(default=True)
    reserved = models.BooleanField(default=False)
    bought = models.BooleanField(default=False)
    price_for_buyer = models.IntegerField()
    note = models.TextField(blank=True)
    contract_num = models.CharField(max_length=50)
    contract_date = models.DateTimeField(auto_now_add=True)
    prodaja_detail = models.CharField(max_length=50, choices=ProdajaDetail.choices, default=ProdajaDetail.U_CELOSTI)
    buyer = models.ForeignKey("kupci.Kupac", related_name='ponude', on_delete=models.CASCADE)
    apartment = models.ForeignKey("stanovi.Stan", related_name='ponude', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_or_company_name} - {self.contract_num} {self.price_for_buyer}"

