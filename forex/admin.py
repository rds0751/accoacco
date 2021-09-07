from .models import ExpenseTransaction
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from django import forms
from import_export.admin import ImportExportModelAdmin

class GeneralTransactionAdmin(ImportExportModelAdmin):
    model = ExpenseTransaction
    list_display = ['customer', 'employee', 'value','type','creation_date','status','percent_per_month','payout','amount_left', 'account_number', ]
    fields = [ 'type', 'customer', 'customer_account', 'employee', 'value','value1','doc_date','status','percent_per_month','amount_left', 'notes',  'account_number', 'email']
    list_display_links = ('customer', 'employee')
    search_fields = ('type', 'customer', 'notes')

    def get_queryset(self, request):
        qs = super(GeneralTransactionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter()
        else:
            return qs.filter(owner=request.user)

ra_admin_site.register(ExpenseTransaction, GeneralTransactionAdmin)