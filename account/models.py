from django.db import models
from django.core.validators import MinValueValidator

ACCOUNT_STATUS = [(1, 'Open'), (2, 'Closed')]

class Account(models.Model):
    account_no =models.AutoField(primary_key = True)
    name = models.CharField(max_length = 50, blank = False)
    email_id = models.CharField(blank = False, unique = True, max_length = 50)
    balance_amount = models.FloatField(blank = False, validators=[MinValueValidator(0.0)])
    status = models.IntegerField(choices = ACCOUNT_STATUS, default = 1)
