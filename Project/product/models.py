from django.db import models
from django.utils import tree
from django.utils.translation import ugettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse
class Product(models.Model):
 PRDname=models.CharField(max_length=100,verbose_name=_("Name") )
 PRDCategory=models.ForeignKey('category',on_delete=models.CASCADE,null=True,blank=True,verbose_name=_("category"))
 PRDBrand=models.ForeignKey("settings.Brand",on_delete=models.CASCADE,null=True,blank=True ,verbose_name=_("Brand"))
 PRDdesc=models.TextField(verbose_name=_("Prodtuct Descrption"))
 PRDImage=models.ImageField(upload_to='IMAGE', verbose_name=_("IMAGE"),null=True,blank=True)
 PRDprice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Prodtuct Price"))
 PRDDiscountPrice=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Discount Price"))
 PRDcost=models.DecimalField(max_digits=5,decimal_places=2,verbose_name=_("Prodtuct Cost"))
 PRDcreated =models.DateTimeField(verbose_name=_("Created At"))
 PRDslug=models.SlugField(blank=True,null=True)
 PRDNew=models.BooleanField(default=True)
 PRDBestSeller=models.BooleanField(default=False)
 def __str__(self):
      return self.PRDname
 def  save(self,*args,**kwargs):
   if not self.PRDslug :
     self.PRDslug=slugify(self.PRDname)
     super(Product , self).save(*args,**kwargs)
  
 def get_absolute_url(self):
    return reverse('products:product_detail', kwargs={'slug': self.PRDslug})

class meta():
   verbose_name=_('product')
   verbose_name_plueal=_('products')

class ProductImage(models.Model):
 PRDIProduct=models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name=_("Product"))
 PRDIImage=models.ImageField(upload_to='IMAGE', verbose_name=_("IMAGE"))
    
 def __str__(self):
     return  self.PRDIProduct 

class category(models.Model):
 CATMain_Category=models.CharField(max_length=100,verbose_name=_("Name"))
 CATParent=models.ForeignKey('self',limit_choices_to={'CATParent__isnull':True} ,verbose_name=_("Main category"), on_delete=models.CASCADE,blank=True,null=True)
 CAtDesc=models.TextField( verbose_name=_("Description"))
 CATimg=models.ImageField(upload_to='category/',verbose_name=_("Image"))
 class Meta:
  verbose_name =_("categorry")
  verbose_name_plural = _("categories")

 def __str__(self):
    return  self.CATMain_Category 

class Product_Alterative(models.Model):
 PALNProducte=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="Main_Product",verbose_name=_("Producte"))
 PLANAlterative=models.ManyToManyField(Product,related_name="Alterative_Product",verbose_name=_("Alterative"))
 
 class Meta:
   verbose_name =_("Product Alterative")
   verbose_name_plural = _("Product Alteratives")

 def __str__(self):
    return str(self.PALNProducte ) 
     
     
     
class Product_Accessories(models.Model):
   PACCProducte=models.ForeignKey(Product,on_delete=models.CASCADE,related_name="MainAccessories_Product",verbose_name=_("Producte"))
   PACCAccessories=models.ManyToManyField(Product,related_name="Accessories_Product" ,verbose_name=_("Accessories"))
 
   class Meta:
    verbose_name =_("Product Accessories")
    verbose_name_plural = _("Product Accessories")

    def __str__(self):
      return  self.CATMain_Category 
     