# from django.contrib import admin
# from ra.admin.admin import ra_admin_site

# # Register your models here.

# from django.contrib.auth.models import User
# from accounting.models import  AccountYear,AccountType,Ledger,Transaction,TransactionDetails,JournalEntry

# class AccountYearAdmin(admin.ModelAdmin):
#     model = AccountYear

# class AccountTypeAdmin(admin.ModelAdmin):
#     model = AccountType

# class TransactionDetailsInline(admin.TabularInline):
#     model = TransactionDetails
#     extra = 1     

# class TransactionAdmin(admin.ModelAdmin):
#     model = Transaction
#     list_display = ('subject','ref_no','account_year','voucher_no','entry_date','post_status')
#     inlines = [TransactionDetailsInline]

# class JournalEntryAdmin(admin.ModelAdmin):
#     model = JournalEntry  

# class LedgerAdmin(admin.ModelAdmin):
#     model = Ledger      
         
# ra_admin_site.register(AccountYear, AccountYearAdmin)   
# ra_admin_site.register(AccountType, AccountTypeAdmin)  
# ra_admin_site.register(Ledger, LedgerAdmin)  
# ra_admin_site.register(Transaction, TransactionAdmin)  
# ra_admin_site.register(JournalEntry, JournalEntryAdmin)
    


