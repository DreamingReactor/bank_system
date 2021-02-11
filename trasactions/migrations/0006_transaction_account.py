# Generated by Django 3.1.6 on 2021-02-09 21:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
        ('trasactions', '0005_remove_transaction_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='account.account'),
            preserve_default=False,
        ),
    ]
