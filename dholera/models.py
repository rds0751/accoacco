from django.db import models
from hr.models import Employee
from utility.models import Unit,BaseModel
from crm.models  import Supplier,Customer,BillingAddress

from django.utils.translation import ugettext_lazy as _
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel


class WareHouse(BaseModel):
    code        =  models.CharField(max_length=255, blank=True, null=True) 
    name        =  models.CharField(max_length=255, blank=True, null=True) 
    location    =  models.CharField(max_length=255, blank=True, null=True) 
    date_start  = models.DateField( blank=True, null=True)
    date_end  = models.DateField( blank=True, null=True)
    status = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True)

    class Meta:
        verbose_name = _('Location')
        verbose_name_plural = _('Locations')

    def __str__(self):
        return self.name

class WareHouseManager(models.Model):
    location        = models.ForeignKey(WareHouse, blank=True, null=True,on_delete=models.CASCADE)
    manager         = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
    appointed_date  = models.DateField( blank=True, null=True)
    date_end        = models.DateField( blank=True, null=True)
    status          = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True)

    class Meta:
        verbose_name = _('Location Manager')
        verbose_name_plural = _('Location Managers')

class Category(models.Model):
    parent_colony  = models.ForeignKey('self', blank=True, null=True, default=None, related_name='category_item',on_delete=models.CASCADE)
    name             = models.CharField(max_length=255, blank=True, null=True) 
    description      = models.TextField(blank=True, null=True)
    slug             = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('Colony')
        verbose_name_plural = _('Colonies')

    def __str__(self):
        return self.name

class Item(models.Model):
    location     = models.ForeignKey(WareHouse, blank=True, null=True,on_delete=models.CASCADE)
    colony      = models.ForeignKey(Category, blank=True, null=True,on_delete=models.CASCADE)
    address     = models.CharField(max_length=255, blank=True, null=True) 
    code         = models.CharField(max_length=255, blank=True, null=True) 
    orginal_price = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
    sale_price    = models.DecimalField(default="0.00",max_digits=12,decimal_places=2)
    date_added    = models.DateField( blank=True, null=True)
    slug          = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('Plot')
        verbose_name_plural = _('Plots')


class Sale(TransactionModel):
    customer         = models.ForeignKey(Customer, blank=True, null=True,on_delete=models.CASCADE)
    seller           = models.ForeignKey(Employee, blank=True, null=True,on_delete=models.CASCADE)
    status           = models.CharField(max_length=32, choices=(('order_submitted','order_submitted'),
        ('shipping_registry','shipping_registry'),
        ('completed','completed'),
        ('back','back'),
        ('order_cancel','order_cancel')
        ), blank=True)

    class Meta:
        verbose_name = _('Sale')
        verbose_name_plural = _('Sales')

class SaleProducts(QuantitativeTransactionItemModel):
    sale         = models.ForeignKey(Sale, blank=True, null=True,on_delete=models.CASCADE)
    plot         = models.ForeignKey(Item, blank=True, null=True,on_delete=models.CASCADE)
    date_added   = models.DateField( blank=True, null=True)
    slug         = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = _('Plot Sold')
        verbose_name_plural = _('Plots Sold')