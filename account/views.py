from account.models import Account
from account.serializer import AccountBalanceSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated

class ShowBalance(RetrieveAPIView):
    serializer_class = AccountBalanceSerializer
    lookup_field = 'account_no'
    queryset = Account.objects.filter(status = 1)
