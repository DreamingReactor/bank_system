from django.apps import AppConfig
from django.db.models.signals import post_migrate

class AccountConfig(AppConfig):
    name = 'account'
    def ready(self):
        import account.models as account_model
        from account.signals import auto_increment_start
        post_migrate.connect(auto_increment_start, sender=account_model)
            