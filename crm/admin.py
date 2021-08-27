from django.contrib import admin
from ra.admin.admin import ra_admin_site

# Register your models here.

from django.contrib.auth.models import User
from crm.models import  Customer,Lead,BillingAddress
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel


class CustomerAdmin(EntityAdmin):
    model = Customer
    fields = ['title','notes','BillingAddress','date_joining','picture','archive_status','status']
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class LeadAdmin(admin.ModelAdmin):
    model = Lead
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class BillingAddressAdmin(admin.ModelAdmin):
    model = BillingAddress
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


ra_admin_site.register(Lead, LeadAdmin) 
ra_admin_site.register(Customer, CustomerAdmin)
ra_admin_site.register(BillingAddress, BillingAddressAdmin)
