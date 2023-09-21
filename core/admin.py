from django.contrib import admin
from core.models import Transaction

class TransactionAdmin(admin.ModelAdmin):
    list_editable = ['amount', 'status', 'transaction_type', 'reciever', 'sender']
    list_display = ['user', 'amount', 'status', 'transaction_type', 'reciever', 'sender']

admin.site.register(Transaction, TransactionAdmin)
# Register your models here.
