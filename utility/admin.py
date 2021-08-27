from django.contrib import admin
from ra.admin.admin import ra_admin_site

# Register your models here.

from django.contrib.auth.models import User
from ra.admin.admin import ra_admin_site, EntityAdmin, TransactionAdmin, TransactionItemAdmin
from utility.models import  UserProfile,Company,CompanyBranch,PredfinedPointsRule,Unit,BusinessType,Tax,Vat,AddressBaseModel

class AddressBaseModelAdmin(admin.ModelAdmin):
    model = AddressBaseModel
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class CompanyBranchInline(admin.StackedInline):
    model = CompanyBranch
    extra = 1
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class CompanyAdmin(EntityAdmin):
    model = Company
    inlines = [CompanyBranchInline,]
    fields = ['title','notes','description','email','cell_phone','land_phone','country','state','city','zip_code','about','contact_details','latitude','longitude','year_established','total_employees','business_type','main_products','total_annual_revenue','url','social_link']

class PredfinedPointsRuleAdmin(admin.ModelAdmin):
    model = PredfinedPointsRule
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class UnitAdmin(admin.ModelAdmin):
    model = Unit
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class BusinessTypeAdmin(admin.ModelAdmin):
    model = BusinessType
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class TaxAdmin(admin.ModelAdmin):
    model = Tax
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}

class VatAdmin(admin.ModelAdmin):
    model = Vat
    def get_model_perms(self, request):
        """
        Return empty perms dict thus hiding the model from admin index.
        """
        return {}


# ra_admin_site.register(UserProfile, UserProfileAdmin)
# ra_admin_site.register(Company, CompanyAdmin)
# ra_admin_site.register(PredfinedPointsRule, PredfinedPointsRuleAdmin)
# ra_admin_site.register(Unit, UnitAdmin)
# ra_admin_site.register(BusinessType, BusinessTypeAdmin)
# ra_admin_site.register(Tax, TaxAdmin)
# ra_admin_site.register(Vat, VatAdmin)
