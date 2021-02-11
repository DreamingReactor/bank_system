from rest_framework.serializers import ModelSerializer
from trasactions.models import Transaction
from account.models import Account

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = ('id', 'account', 'type', 'amount')

# class GenerateExcelSerializer(ModelSerializer)