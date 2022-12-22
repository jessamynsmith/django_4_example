from django.urls import path

from my_app import views


urlpatterns = [
    path('transaction_logs/', views.TransactionLogListView.as_view(), name='transaction-logs-list'),
    path('transaction_logs/create/', views.TransactionLogCreateView.as_view(), name='transaction-logs-create'),
]
