# Generated by Django 3.1.6 on 2021-02-09 21:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField(choices=[(1, 'Deposit'), (2, 'Withdraw')])),
                ('amount', models.FloatField(validators=[django.core.validators.MinValueValidator(1.0)])),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='account.account')),
            ],
        ),
    ]
