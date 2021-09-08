from .models import ExpenseTransaction, NewExpenseTransaction, NewExpenseTransaction1
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
    fields = [ 'customer', 'customer_account', 'employee', 'value','value1','type','doc_date','status','percent_per_month','amount_left', 'notes', 'file']
    list_display_links = ('customer', 'employee')
    search_fields = ('customer', 'notes')


    def get_queryset(self, request):
        qs = super(GeneralTransactionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter()
        else:
            return qs.filter(owner=request.user)

class NewTransactionAdmin(ImportExportModelAdmin):
    model = NewExpenseTransaction
    list_display = [ 'customer','employee', 'value','type','creation_date']
    fields = [ 'customer', 'account', 'employee', 'value','value1','type','doc_date','notes']
    list_display_links = ('customer', 'employee')
    search_fields = ('customer', 'notes')


    def get_queryset(self, request):
        qs = super(NewTransactionAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter()
        else:
            return qs.filter(owner=request.user)

class NewTransactionAdmin1(ImportExportModelAdmin):
    model = NewExpenseTransaction1
    list_display = [ 'customer','employee', 'value','creation_date']
    fields = [ 'customer', 'account', 'employee', 'value','value1','doc_date','notes', 'image']
    list_display_links = ('customer', 'employee')
    search_fields = ('customer', 'notes')


    def get_queryset(self, request):
        qs = super(NewTransactionAdmin1, self).get_queryset(request)
        if request.user.is_superuser:
            return qs.filter()
        else:
            return qs.filter(owner=request.user)


ra_admin_site.register(ExpenseTransaction, GeneralTransactionAdmin)
ra_admin_site.register(NewExpenseTransaction, NewTransactionAdmin)
ra_admin_site.register(NewExpenseTransaction1, NewTransactionAdmin1)