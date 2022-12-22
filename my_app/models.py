from uuid import uuid4

from django.conf import settings
from django.db import models


class TransactionLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    transaction_id = models.UUIDField(default=uuid4)
    notes = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.transaction_id}: {self.notes} ({self.created_at})'

    def localized_created_at(self):
        print(self.created_at)
        as_default = self.created_at.astimezone(settings.DEFAULT_TIME_ZONE)
        print(as_default)
        return as_default
