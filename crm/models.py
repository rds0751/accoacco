from django.db import models
from django.contrib.auth.models import User
from utility.models import UserProfileBaseModel,BaseModel,BusinessType,AddressBaseModel
from ra.base.models import EntityModel, TransactionModel, TransactionItemModel, QuantitativeTransactionItemModel

from hr.models import Employee
# Create your models here.


class BillingAddress(AddressBaseModel): 
  pass

class Lead(UserProfileBaseModel):
   date_entry     = models.DateField( blank=True, null=True)	
   archive_status = models.CharField(max_length=32, choices=(('yes','yes'),('no','no')), blank=True) 
   status         = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 


class Customer(EntityModel):
    BillingAddress    = models.ForeignKey(BillingAddress, related_name="CustomerBillingAddress", blank=True, null=True,on_delete=models.CASCADE)
    date_joining      = models.DateField( blank=True, null=True) 
    picture           = models.FileField(upload_to='documents/%Y/%m/%d',blank=True, null=True)     
    archive_status    = models.CharField(max_length=32, choices=(('yes','yes'),('no','no')), blank=True) 
    status            = models.CharField(max_length=32, choices=(('active','active'),('inactive','inactive')), blank=True) 
    
    def get_full_name(self):
          return self.user.first_name+" "+self.user.last_name

class Supplier(UserProfileBaseModel):
    user              = models.OneToOneField(User, related_name="Supplier", on_delete=models.CASCADE)
    BillingAddress    = models.ForeignKey(BillingAddress, related_name="SupplierBillingAddress", blank=True, null=True,on_delete=models.CASCADE)
    license_number    = models.CharField(verbose_name=("License number"),max_length=127)
    business_type     = models.ForeignKey(BusinessType, related_name="SupplierBusinessType", blank=True, null=True,on_delete=models.CASCADE)
    
    def get_full_name(self):
          return self.user.first_name+" "+self.user.last_name
    
    def __str__(self):
          return self.user.username  

         
  