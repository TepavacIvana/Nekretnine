from django.db import models


class Stan(models.Model):
    advertised = models.DateTimeField(auto_now_add=True)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    lamella = models.CharField(max_length=20)
    size = models.CharField(max_length=20)
    floor = models.IntegerField()
    num_of_rooms = models.FloatField()
    orientation = models.CharField(max_length=30)
    num_of_terraces = models.IntegerField()
    price = models.IntegerField()
    available = models.BooleanField(default=True)
    reserved = models.BooleanField(default=False)
    sold = models.BooleanField(default=False)
    image = models.ImageField(upload_to='static/images/', default='static/images/stan.jpg')
    owner = models.ForeignKey("korisnici.Korisnik", related_name='stanovi', on_delete=models.CASCADE)
    buyer = models.ForeignKey("kupci.Kupac", related_name='stanovi', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        # ordering = ['-advertised']
        ordering = ['price']            # ascending
        # ordering = ['-price']           # descending

    def __str__(self):
        return self.address

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
