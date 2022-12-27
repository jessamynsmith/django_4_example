from django.conf import settings
from django.urls import reverse_lazy
from django.utils import timezone
from django.views.generic import CreateView, ListView

from my_app import models as my_app_models
from my_app.helpers import localized_datetime


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
    fields = ['transaction_id', 'transaction_date', 'notes']
    success_url = reverse_lazy('transaction-logs-list')

    def dispatch(self, request, *args, **kwargs):
        # In a fully implemented application, this would be the user's selected timezone.
        timezone.activate(settings.DEFAULT_TIME_ZONE)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)
        context_data['time_zone'] = settings.DEFAULT_TIME_ZONE
        return context_data

    def get_initial(self):
        initial = super().get_initial()
        initial['transaction_date'] = localized_datetime(
            settings.DEFAULT_TIME_ZONE, timezone.now())
        return initial
