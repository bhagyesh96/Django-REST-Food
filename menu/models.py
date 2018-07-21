from django.db import models
from seller.models import sellerDetails
from datetime import date
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver

# Create your models here.

class menulist(models.Model):
    seller = models.ForeignKey(sellerDetails,on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    cuisin = models.CharField(max_length=100)
    menu = models.CharField(max_length=700)
    price = models.IntegerField()
    expires = models.TimeField()
    aval = models.IntegerField()
    menuPic = models.ImageField()


@receiver(pre_delete, sender=menulist)
def restroPic_delete(sender, instance, **kwargs):
    instance.menuPic.delete(False)





