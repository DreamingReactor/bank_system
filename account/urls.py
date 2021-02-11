from django.urls import path
from account.views import ShowBalance

urlpatterns = [
    path('check_balance/<int:account_no>', ShowBalance.as_view(), name = 'show_balance'),
]