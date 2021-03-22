from django.db import models

class Beer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    abv = models.FloatField(unique=False)
    description = models.CharField(max_length=500)
    image = models.CharField(max_length=300)
    keg_size = models.PositiveIntegerField(unique=False)
    keg_price = models.FloatField(unique=False)

    def __str__(self):
        return f'{self.name} - {self.abv}%'
        