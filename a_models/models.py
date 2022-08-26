from django.db import models

# Create your models here.
class UniwareMaster(models.Model):
    uniware = models.CharField(max_length = 70)
    brand = models.CharField(max_length = 70)
    headcat = models.CharField(max_length = 70)
    subcat = models.CharField(max_length = 70)
    productpic = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.uniware

class UniwareDimension(models.Model):
    uniware = models.OneToOneField(UniwareMaster, on_delete=models.CASCADE)
    length = models.IntegerField()
    width = models.IntegerField()
    height = models.IntegerField()

    def __str__(self):
        return self.uniware

class Inbound(models.Model):
    uniware = models.ForeignKey(UniwareMaster, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.IntegerField()

    def __str__(self):
        return self.uniware
    