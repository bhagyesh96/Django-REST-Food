from django.db import models
from django.core.validators import RegexValidator

# Create your models here.

class sellerDetails(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    PhoneNo = models.CharField(validators=[phone_regex], blank=True, max_length=12,
                               unique=True)  # validators should be a list
    Address = models.CharField(max_length=300)
    city = models.CharField(max_length=100)
    BrandName = models.CharField(max_length=100, unique=True)
    premium = models.BooleanField(default=False)
    verify = models.BooleanField(default=False)

    def __iter__(self):
        return iter(self.BrandName)











