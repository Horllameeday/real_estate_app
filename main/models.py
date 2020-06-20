from django.db import models
from django.contrib.auth.models import User

# Create your models here.

FACILITY_TYPES = (
    ('L', 'Land'),
    ('A', 'Apartment'),
    ('R', 'Rental'),
)

class Vendor(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=500)
    contact = models.CharField(max_length=15)

    def __str__(self):
        return self.name

class Facility(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=100)
    image = models.FileField()
    image_2 = models.FileField()
    image_3 = models.FileField()
    price = models.FloatField(default=1)
    description = models.TextField(blank=True, null=True)
    vendor = models.ForeignKey(Vendor, related_name='facilities', on_delete=models.SET_NULL, blank=True, null=True)
    facility_type = models.CharField(max_length=20, choices=FACILITY_TYPES)
    featured = models.BooleanField(default=False)
    slug = models.SlugField()

    def __str__(self):
        return self.name