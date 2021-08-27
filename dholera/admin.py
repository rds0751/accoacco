from django.contrib import admin
from ra.admin.admin import ra_admin_site, TransactionAdmin, TransactionItemAdmin

from dholera.models  import Category,Item,SaleProducts,Sale
# Register your models here.

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1 


class CategoryAdmin(admin.ModelAdmin):
    model = Category

class ItemAdmin(admin.ModelAdmin):
    model = Item
    list_display = [f.name for f in Item._meta.fields]

class SaleProductsInline(TransactionItemAdmin):
    model = SaleProducts
    fields = ('plot', 'price', 'quantity')
    extra = 1

class SaleAdmin(TransactionAdmin):
    model = Sale
    inlines = [SaleProductsInline]
    fields = ['slug', 'doc_date', 'customer_id', 'employee']
    copy_to_formset = ['customer_id', 'employee']
    add_form_template = change_form_template = 'erplogic/admin/sales_change_form.html'

    def formfield_for_dbfield(self, db_field, request, **kwargs):
        formfield = super().formfield_for_dbfield(db_field, request, **kwargs)
        if db_field.name == 'value':
            formfield.widget = forms.TextInput(attrs={'readonly': 'readonly'})
        return formfield

ra_admin_site.register(Category, CategoryAdmin) 
ra_admin_site.register(Item, ItemAdmin) 
ra_admin_site.register(Sale, SaleAdmin)