from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from my_app import models as my_app_models


class TransactionLogListView(ListView):
    model = my_app_models.TransactionLog


class TransactionLogCreateView(CreateView):
    model = my_app_models.TransactionLog
    fields = ['transaction_id', 'notes']
    success_url = reverse_lazy('transaction-logs-list')
