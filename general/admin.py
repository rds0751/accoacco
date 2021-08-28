from .models import ExpenseTransaction, NewExpenseTransaction
from import_export.admin import ImportExportModelAdmin
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from django import forms
from import_export import resources

class GeneralResource(resources.ModelResource):
    class Meta:
        model = ExpenseTransaction
        fields = ['id', 'customer', 'value','type','doc_date','status','percent_per_month','amount_left', 'notes', 'lastmod_user']

class GeneralTransactionAdmin(ImportExportModelAdmin):
    model = ExpenseTransaction
    resource_class = GeneralResource
    list_display = [ 'customer', 'employee', 'value','type','creation_date','status','percent_per_month','payout','amount_left']
    fields = [ 'customer', 'employee', 'value','type','doc_date','status','percent_per_month','amount_left', 'notes']
    list_display_links = ('customer', 'employee')
    search_fields = ('customer', 'notes')

class NewTransactionAdmin(ImportExportModelAdmin):
    model = NewExpenseTransaction
    list_display = [ 'customer', 'employee', 'value','type','creation_date','status','percent_per_month','payout','amount_left']
    fields = [ 'customer', 'employee', 'value','type','doc_date','status','percent_per_month','amount_left', 'notes']
    list_display_links = ('customer', 'employee')
    search_fields = ('customer', 'notes')

ra_admin_site.register(ExpenseTransaction, GeneralTransactionAdmin)
ra_admin_site.register(NewExpenseTransaction, NewTransactionAdmin)