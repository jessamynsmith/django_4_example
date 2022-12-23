from uuid import uuid4

from django.conf import settings
from django.db import models

from my_app.helpers import localized_datetime


class TransactionLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_date = models.DateTimeField()
    transaction_id = models.UUIDField(default=uuid4)
    notes = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.transaction_id}: {self.notes} ({self.created_at})'

    def localized_created_at(self):
        as_default = localized_datetime(settings.DEFAULT_TIME_ZONE, self.created_at)
        return as_default

    def localized_transaction_date(self):
        as_default = localized_datetime(settings.DEFAULT_TIME_ZONE, self.transaction_date)
        return as_default
