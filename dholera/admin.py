from django.contrib import admin
from ra.admin.admin import ra_admin_site, TransactionAdmin, TransactionItemAdmin

from dholera.models  import WareHouse,WareHouseManager,Category,Item,SaleProducts,Sale
# Register your models here.

class WareHouseManagerInline(admin.TabularInline):
    model = WareHouseManager
    extra = 1     

class ItemInline(admin.TabularInline):
    model = Item
    extra = 1 

class WareHouseAdmin(admin.ModelAdmin):
    model = WareHouse
    inlines = [WareHouseManagerInline]

class CategoryAdmin(admin.ModelAdmin):
    model = Category

class ItemAdmin(admin.ModelAdmin):
    model = Item

class SaleProductsInline(TransactionItemAdmin):
    model = SaleProducts
    fields = ('plot', 'price', 'quantity')
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

ra_admin_site.register(WareHouse, WareHouseAdmin) 
ra_admin_site.register(Category, CategoryAdmin) 
ra_admin_site.register(Item, ItemAdmin) 
ra_admin_site.register(Sale, SaleAdmin)