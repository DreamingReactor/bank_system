# Generated by Django 3.1.6 on 2021-02-09 21:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trasactions', '0004_transaction_account'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='account',
        ),
    ]