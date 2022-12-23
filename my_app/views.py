from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from my_app import models as my_app_models


class TransactionLogListView(ListView):
    model = my_app_models.TransactionLog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('transaction_id', '-id').distinct('transaction_id')
        return queryset


class TransactionLogCreateView(CreateView):
    model = my_app_models.TransactionLog
    fields = ['transaction_id', 'notes']
    success_url = reverse_lazy('transaction-logs-list')
