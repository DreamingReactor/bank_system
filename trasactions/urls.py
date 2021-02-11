from django.urls import path
from trasactions.views import Withdraw, Deposit, GenerateExcel

urlpatterns = [
    path('withdraw', Withdraw.as_view(), name = 'withdraw'),
    path('deposit', Deposit.as_view(), name = 'deposit'),
    path('generate_xl', GenerateExcel.as_view(), name = 'generate_xl'),
]