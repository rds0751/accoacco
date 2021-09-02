from django.contrib import admin
from ra.admin.admin import ra_admin_site, TransactionAdmin, TransactionItemAdmin

from dholera.models  import Category
# Register your models here.

from .models import ExpenseTransaction
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from django import forms

class DholeraTransactionAdmin(TransactionAdmin):
    model = ExpenseTransaction
    list_display = ['customer', 'employee','project', 'plot_number', 'value','creation_date','status','amount_left']
    fields = ['customer', 'customer_account', 'employee','project', 'plot_number', 'value','doc_date','status','amount_left', 'notes']
    list_display_links = ('customer', 'employee')
    search_fields = ('customer', 'notes')

    def get_queryset(self, request):
        qs = super(DholeraTransactionAdmin, self).get_queryset(request)
        return qs.filter(owner=request.user)


class CategoryAdmin(admin.ModelAdmin):
    model = Category


ra_admin_site.register(Category, CategoryAdmin)
ra_admin_site.register(ExpenseTransaction, DholeraTransactionAdmin)
