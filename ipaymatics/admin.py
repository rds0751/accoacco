from .models import ExpenseTransaction
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from django import forms

from import_export.admin import ImportExportModelAdmin

from import_export import resources

class IpaymaticsResource(ImportExportModelAdmin):
    class Meta:
        model = ExpenseTransaction
        fields = [  'customer','upline', 'userID', 'contact',  'employee', 'value','status','amount_left','notes']

class IpaymaticsTransactionAdmin(TransactionAdmin):
    model = ExpenseTransaction
    resource_class = IpaymaticsResource
    list_display = [  'customer','upline', 'userID', 'contact',  'employee', 'value','creation_date','status','amount_left']
    fields = [  'customer', 'customer_account', 'upline', 'userID', 'contact',  'employee', 'value','doc_date','status','amount_left','notes']
    list_display_links = ( 'customer', 'employee')
    search_fields = ( 'customer', 'notes')

ra_admin_site.register(ExpenseTransaction, IpaymaticsTransactionAdmin)