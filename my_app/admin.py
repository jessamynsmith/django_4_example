from django.contrib import admin

from my_app import models


class TransactionLogAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction_id', 'notes', 'created_at']


admin.site.register(models.TransactionLog, TransactionLogAdmin)
