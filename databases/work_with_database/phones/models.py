from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=21)
    price = models.DecimalField(max_digits=5, decimal_places=0)
    image = models.CharField(max_length=90)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField()
