from django.db import models
from django.utils.translation import ugettext_lazy as _

class Brand(models.Model):
    BRDName=models.CharField(max_length=40,verbose_name="Name" )
    BRDDesc=models.TextField(null=True,blank=True ,verbose_name="Description")

    class Meta:
      verbose_name=_('Brand')
      verbose_name_plural=_('Brands')

    def __str__(self):
       return  self.BRDName

class variant(models.Model):
    VARName=models.CharField(max_length=40)
    VARDesc=models.TextField(blank=True,null=True)

    class meta:
        verbose_name=_("variant")
        verbose_name_plural=("variants")
    
    def __str__(self):
        return self.VARName
        

  


