from trasactions.notify import send_email
import json

class TransactionOperation():
    def deposit(transaction_obj):
        account_obj = transaction_obj.account
        if account_obj:
            amount = transaction_obj.amount
            account_obj.balance_amount += amount
            account_obj.save()
            mail_sent = send_email(account_obj.name, account_obj.email_id, transaction_obj.amount, account_obj.account_no, account_obj.balance_amount, 1, transaction_obj.transaction_time)
            if not mail_sent:
                transaction_obj.remark = 'Email notification failed.'
            transaction_obj.status = 1
            transaction_obj.save()
            response = json.dumps({'success': True, 'message': 'Transaction successful'})
        else:
            transaction_obj.status = 2
            transaction_obj.remark = 'Account does not exist or has been closed.'
            transaction_obj.save()
            response = json.dumps({'success': False, 'message': transaction_obj.remark})
    
    def withdraw(transaction_obj):
        account_obj = transaction_obj.account
        if account_obj:
            amount = transaction_obj.amount
            if account_obj.balance_amount > amount:
                account_obj.balance_amount -= amount
                account_obj.save()
                mail_sent = send_email(account_obj.name, account_obj.email_id, transaction_obj.amount, account_obj.account_no, account_obj.balance_amount, 2, transaction_obj.transaction_time)
                if not mail_sent:
                    transaction_obj.remark = 'Email notification failed.'
                transaction_obj.status = 1
                transaction_obj.save()
                response = json.dumps({'success': True, 'message': 'Transaction successful'})
            else:
                transaction_obj.status = 2
                transaction_obj.remark = 'Balance too low.'
                transaction_obj.save()
                response = json.dumps({'success': False, 'message': transaction_obj.remark})
        else:
            transaction_obj.status = 2
            transaction_obj.remark = 'Account does not exist or has been closed.'
            transaction_obj.save()
            response = json.dumps({'success': False, 'message': transaction_obj.remark})