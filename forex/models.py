from django.db import models

from hr.models import Employee
from utility.models import Unit,BaseModel
from crm.models  import Supplier,Customer,BillingAddress
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel
from ra.base.registry import register_doc_type
from django.utils.translation import ugettext_lazy as _


class Sale(TransactionModel):
    customer         = models.ForeignKey(Customer, related_name='forex_customer', blank=True, null=True,on_delete=models.CASCADE)
    seller           = models.ForeignKey(Employee, related_name='forex_seller', blank=True, null=True,on_delete=models.CASCADE)
    status           = models.CharField(max_length=32, choices=(('order_submitted','order_submitted'),
        ('roi started','roi started'),
        ('completed','completed')
        ), blank=True)

    class Meta:
        verbose_name = _('Sale')
        verbose_name_plural = _('Sales')

class SaleProducts(QuantitativeTransactionItemModel):
    sale         = models.ForeignKey(Sale, related_name='forex_sale', blank=True, null=True,on_delete=models.CASCADE)
    date_added   = models.DateField(blank=True, null=True)
    slug         = models.CharField(max_length=255, blank=True, null=True)
    roi          = models.DecimalField(blank=True, null=True, max_digits=3, decimal_places=2)

    class Meta:
        verbose_name = _('Total amount')
        verbose_name_plural = _('total amount')