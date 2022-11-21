from django.db import models

# Create your models here.
class doctors(models.Model):

    dr_name=models.CharField(max_length=15)
    specialist =models.CharField(max_length=15)
    appointments =models.IntegerField()

    def __str__(self):
        return self.dr_name
