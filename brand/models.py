from django.db import models  

class Brand(models.Model):
    name= models.CharField(max_length=255, verbose_name='Brand') 

    def __str__(self):
        return f'brand name:{self.name}'