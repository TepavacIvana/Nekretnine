from django.db import models


class Kupac(models.Model):
    full_or_company_name = models.CharField(max_length=80, blank=True, null=True)
    citizen = models.BooleanField(default=True)
    company = models.BooleanField(default=False)
    email = models.EmailField(unique=False)
    phone_num = models.IntegerField()
    PIB_JMBG = models.IntegerField()
    address = models.CharField(max_length=100)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.full_or_company_name

