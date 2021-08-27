from django.db import models

from hr.models import Employee
from utility.models import Unit,BaseModel
from crm.models  import Supplier,Customer,BillingAddress
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel
from ra.base.registry import register_doc_type
from django.utils.translation import ugettext_lazy as _


class ExpenseTransaction(TransactionModel):
    customer         = models.CharField(max_length=256, blank=True, null=True)
    employee           = models.ForeignKey(Employee, related_name='general_transaction_employee', blank=True, null=True,on_delete=models.CASCADE)
    status           = models.CharField(max_length=32, choices=(('unpaid','unpaid'),
        ('partial','partial'),
        ('completed','completed')
        ), blank=True)
    percent_per_month = models.DecimalField(max_digits=5, decimal_places=2)
    sponsor = models.ForeignKey(Customer, related_name='general_transaction_sponsor', null=True, blank=True, on_delete=models.CASCADE)
    amount_left = models.IntegerField(default=0)
    type = models.CharField(max_length=32, choices=(('cheque','cheque'),
        ('credit','credit'),
        ('debit','debit')
        ), blank=True)

    def payout(self):
    	return self.percent_per_month * self.value / 100

    class Meta:
        verbose_name = _('General Transaction')
        verbose_name_plural = _('General Transactions')
