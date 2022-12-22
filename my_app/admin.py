from django.contrib import admin

from my_app import models


admin.site.register(models.TransactionLog)
