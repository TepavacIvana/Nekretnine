from django.db import models


class Kupac(models.Model):

    class KupacStatus(models.TextChoices):
        CITIZEN = 'Citizen', 'Citizen'
        COMPANY = 'Company', 'Company'

    id_kupca = models.BigAutoField(db_column='id_kupca', primary_key=True)
    full_or_company_name = models.CharField(max_length=80, blank=True, null=True)
    status_buyer = models.CharField('Status', max_length=50,
                                    choices=KupacStatus.choices,
                                    default=KupacStatus.CITIZEN,
                                    blank=False,
                                    null=False)
    email = models.EmailField(unique=False)
    phone_num = models.IntegerField()
    PIB_JMBG = models.IntegerField()
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id_kupca']

    def __str__(self):
        return f"{self.id_kupca}, {self.full_or_company_name}"
