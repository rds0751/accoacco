from django.db import models

from hr.models import Employee
from utility.models import Unit,BaseModel
from crm.models  import Supplier,Customer,BillingAddress
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel
from ra.base.registry import register_doc_type
from django.utils.translation import ugettext_lazy as _


class ExpenseTransaction(TransactionModel):
    customer         = models.CharField(max_length=256, blank=True, null=True)
    customer_account = models.ForeignKey(Customer, related_name='general_transaction_customer', blank=True, null=True,on_delete=models.CASCADE)
    employee           = models.ForeignKey(Employee, related_name='general_transaction_employee', blank=True, null=True,on_delete=models.CASCADE)
    status           = models.CharField(max_length=32, choices=(('unpaid','unpaid'),
        ('partial','partial'),
        ('completed','completed')
        ), blank=True, null=True)
    percent_per_month = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    sponsor = models.ForeignKey(Customer, related_name='general_transaction_sponsor', null=True, blank=True, on_delete=models.CASCADE)
    amount_left = models.IntegerField(default=0)
    file = models.FileField(null=True, blank=True)
    type = models.CharField(max_length=32, choices=(('cheque','cheque'),
        ('credit','credit'),
        ('debit','debit')
        ), blank=True, null=True)

    def payout(self):
        try:
            a = self.percent_per_month * self.value / 100
        except Exception as e:
            a = 0
        return a

    class Meta:
        verbose_name = _('General Transaction')
        verbose_name_plural = _('General Transactions')

    # def __str__(self):
    #     return self.customer

class NewExpenseTransaction(TransactionModel):
    customer         = models.CharField(max_length=256, blank=True, null=True)
    account = models.ForeignKey(Customer, related_name='daily_transaction_customer', blank=True, null=True,on_delete=models.CASCADE)
    employee           = models.ForeignKey(Employee, related_name='daily_transaction_employee', blank=True, null=True,on_delete=models.CASCADE)
    type = models.CharField(max_length=32, choices=(('cheque','cheque'),
        ('credit','credit'),
        ('debit','debit')
        ), blank=True, null=True)

    def payout(self):
        try:
            a = self.percent_per_month * self.value / 100
        except Exception as e:
            a = 0
        return a

    class Meta:
        verbose_name = _('Daily Transaction')
        verbose_name_plural = _('Daily Transactions')

    # def __str__(self):
    #     return self.customer

class NewExpenseTransaction1(TransactionModel):
    customer         = models.CharField(max_length=256, blank=True, null=True)
    account = models.ForeignKey(Customer, related_name='withdrawal_customer', blank=True, null=True,on_delete=models.CASCADE)
    employee           = models.ForeignKey(Employee, related_name='withdrawal_employee', blank=True, null=True,on_delete=models.CASCADE)
    image = models.FileField(null=True, blank=True)

    class Meta:
        verbose_name = _('Withdrawal')
        verbose_name_plural = _('Withdrawals')

    # def __str__(self):
    #     return self.customer