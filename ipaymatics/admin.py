from .models import SaleProducts,Sale
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from django import forms

class SaleProductsInline(TransactionItemAdmin):
    model = SaleProducts
    fields = ('price', 'quantity')
    extra = 1

class SaleAdmin(TransactionAdmin):
    model = Sale
    inlines = [SaleProductsInline]
    fields = ['slug', 'doc_date', 'customer', 'seller']
    copy_to_formset = ['customer', 'seller']
    add_form_template = change_form_template = 'erplogic/admin/sales_change_form.html'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'value':
            formfield.widget = forms.TextInput(attrs={'readonly': 'readonly'})
        return formfield

ra_admin_site.register(Sale, SaleAdmin)