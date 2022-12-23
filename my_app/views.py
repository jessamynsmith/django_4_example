from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from my_app import models as my_app_models


class TransactionLogListView(ListView):
    model = my_app_models.TransactionLog

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('transaction_id', '-id').distinct('transaction_id')
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['time_zone'] = settings.DEFAULT_TIME_ZONE
        return context_data


class TransactionLogCreateView(CreateView):
    model = my_app_models.TransactionLog
    fields = ['transaction_id', 'notes']
    success_url = reverse_lazy('transaction-logs-list')


# TODO add a view with a form to see if dst is respected
