from django.db import models

# Create your models here.
class Address(models.Model):
    street = models.CharField(max_length=200)
    building = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.street + ' / ' + self.building

class Shop(models.Model):
    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address,related_name='shops',on_delete=models.CASCADE)
    changed_timestamp = models.DateTimeField(auto_now=True)