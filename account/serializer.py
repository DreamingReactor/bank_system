from rest_framework.serializers import ModelSerializer
from account.models import Account

class AccountBalanceSerializer(ModelSerializer):
    class Meta:
        model = Account
        fields = ('account_no','balance_amount')