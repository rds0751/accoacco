from django.db import models

from hr.models import Employee
from utility.models import Unit,BaseModel
from crm.models  import Supplier,Customer,BillingAddress
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel
from ra.base.registry import register_doc_type
from django.utils.translation import ugettext_lazy as _


class ExpenseTransaction(TransactionModel):
    customer         = models.CharField(max_length=256, blank=True, null=True)
    customer_account = models.ForeignKey(Customer, related_name='ipaymatics_transaction_customer', blank=True, null=True,on_delete=models.CASCADE)
    employee           = models.ForeignKey(Employee, related_name='ipaymatics_transaction_employee', blank=True, null=True,on_delete=models.CASCADE)
    status           = models.CharField(max_length=32, choices=(('unpaid','unpaid'),
        ('partial','partial'),
        ('completed','completed')
        ), blank=True, null=True)
    sponsor = models.ForeignKey(Customer, related_name='ipaymatics_transaction_sponsor', null=True, blank=True, on_delete=models.CASCADE)
    amount_left = models.IntegerField(default=0)
    upline = models.CharField(max_length=32, null=True)
    userID = models.CharField(max_length=32, null=True)
    contact = models.CharField(max_length=32, null=True)


    class Meta:
        verbose_name = _('Ipaymatics Transaction')
        verbose_name_plural = _('Ipaymatics Transactions')