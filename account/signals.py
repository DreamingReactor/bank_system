# from django.db.models.signals import post_migrate
from django.db import connection, transaction
# import account.models as account_model

def auto_increment_start(sender, **kwargs):
    cursor = connection.cursor()
    cursor = cursor.execute("""
                                ALTER table account AUTO_INCREMENT=10000000
                            """)
    transaction.commit_unless_managed()
