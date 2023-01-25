from django.contrib import admin

from my_app import models


class ReadonlyMixin:
    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class TransactionLogAdmin(ReadonlyMixin, admin.ModelAdmin):
    list_display = ['id', 'transaction_id', 'notes', 'created_at']


admin.site.register(models.TransactionLog, TransactionLogAdmin)
