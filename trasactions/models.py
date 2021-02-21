from django.db import models
from django.core.validators import MinValueValidator
from account.models import Account
from django.utils import timezone
from bank_system.my_celery import app
from trasactions.transaction_operation import TransactionOperation

TRANSACTION_TYPE = [(1, 'Deposit'), (2, 'Withdraw')]
TRANSACTION_STATUS = [(1, 'Successful'), (2, 'Failed'), (3, 'Processing')]

class Transaction(models.Model):
    type =models.IntegerField(choices = TRANSACTION_TYPE)
    amount = models.FloatField(blank = False, validators=[MinValueValidator(1.0)])
    account = models.ForeignKey(Account, on_delete = models.PROTECT, related_name = 'transaction', null = True)
    status = models.IntegerField(choices = TRANSACTION_STATUS, default = 3)
    transaction_time = models.DateTimeField(default=timezone.now)
    remark = models.CharField(max_length = 100, blank = True)

    def save(self, *args, **kwargs):
        res = super(Transaction, self).save(*args, **kwargs)
        if self.status == 3:
            self.complete_transaction.delay(self.id)
        return res
    
    @app.task
    def complete_transaction(transaction_id):
        transaction_obj = Transaction.objects.get(id = transaction_id)
        if transaction_obj.type == 1:
            response = TransactionOperation.deposit(transaction_obj)
        else:
            response = TransactionOperation.withdraw(transaction_obj)
        return response