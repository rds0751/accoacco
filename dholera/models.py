from django.db import models
from hr.models import Employee
from utility.models import Unit,BaseModel
from crm.models  import Supplier,Customer,BillingAddress
from import_export.admin import ImportExportModelAdmin

from django.utils.translation import ugettext_lazy as _
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel

class Category(models.Model):
    name             = models.CharField(max_length=255, blank=True, null=True) 
    description      = models.TextField(blank=True, null=True)
    slug             = models.CharField(max_length=255, blank=True, null=True)
    total_plots      = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Project')
        verbose_name_plural = _('Projects')

    def __str__(self):
        return self.name

class ExpenseTransaction(TransactionModel):
    customer         = models.CharField(max_length=256, blank=True, null=True)
    employee           = models.ForeignKey(Employee, related_name='dholera_transaction_employee', blank=True, null=True,on_delete=models.CASCADE)
    status           = models.CharField(max_length=32, choices=(('unpaid','unpaid'),
        ('partial','partial'),
        ('completed','completed')
        ), blank=True, null=True)
    sponsor = models.ForeignKey(Customer, related_name='dholera_transaction_sponsor', null=True, blank=True, on_delete=models.CASCADE)
    amount_left = models.IntegerField(default=0)
    type = models.CharField(max_length=32, choices=(('cheque','cheque'),
        ('credit','credit'),
        ('debit','debit')
        ), blank=True, null=True)
    project = models.ForeignKey(Category, on_delete=models.CASCADE)
    plot_number = models.IntegerField(default=0)

    class Meta:
        verbose_name = _('Dholera Transaction')
        verbose_name_plural = _('Dholera Transactions')