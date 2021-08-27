from .models import ExpenseTransaction
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from django import forms

class GeneralTransactionAdmin(TransactionAdmin):
    model = ExpenseTransaction
    list_display = [ 'type', 'customer', 'employee', 'value','creation_date','status','percent_per_month','payout','amount_left']
    fields = [ 'type', 'customer', 'employee', 'value','doc_date','status','percent_per_month','amount_left', 'notes']
    list_display_links = ('type', 'customer', 'employee')
    search_fields = ('type', 'customer', 'notes')

ra_admin_site.register(ExpenseTransaction, GeneralTransactionAdmin)