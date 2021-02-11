from django.db import models
from django.core.validators import MinValueValidator
from account.models import Account
from django.utils import timezone

TRANSACTION_TYPE = [(1, 'Deposit'), (2, 'Withdraw')]
TRANSACTION_STATUS = [(1, 'Successful'), (2, 'Failed'), (3, 'Processing')]

class Transaction(models.Model):
    type =models.IntegerField(choices = TRANSACTION_TYPE)
    amount = models.FloatField(blank = False, validators=[MinValueValidator(1.0)])
    account = models.ForeignKey(Account, on_delete = models.PROTECT, related_name = 'transaction', null = True)
    status = models.IntegerField(choices = TRANSACTION_STATUS, default = 3)
    transaction_time = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length = 100, blank = True)