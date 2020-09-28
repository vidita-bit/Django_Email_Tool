
from django.db import models
# Create your models here.
#from phonenumber_field.modelfields import PhoneNumberField
class Profile(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.name