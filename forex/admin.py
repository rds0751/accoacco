from .models import ExpenseTransaction
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from django import forms

class GeneralTransactionAdmin(TransactionAdmin):
    model = ExpenseTransaction
    list_display = [ 'customer_id', 'employee', 'value','creation_date','status','percent_per_month','payout','amount_left']
    fields = [ 'customer_id', 'employee', 'value','doc_date','status','percent_per_month','amount_left', 'notes']
    list_display_links = ('customer_id', 'employee')
    search_fields = ('customer_id', 'notes')

ra_admin_site.register(ExpenseTransaction, GeneralTransactionAdmin)