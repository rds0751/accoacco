from .models import ExpenseTransaction
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from django import forms

class GeneralTransactionAdmin(TransactionAdmin):
    model = ExpenseTransaction
    list_display = [  'customer','upline', 'userID', 'contact',  'employee', 'value','creation_date','status','amount_left']
    fields = [  'customer','upline', 'userID', 'contact',  'employee', 'value','doc_date','status','amount_left','notes']
    list_display_links = ( 'customer', 'employee')
    search_fields = ( 'customer', 'notes')

ra_admin_site.register(ExpenseTransaction, GeneralTransactionAdmin)