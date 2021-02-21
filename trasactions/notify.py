from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.conf import settings
import pytz

def send_email(name, email, amount, account_no, current_balance, transaction_type, date):
    plaintext = get_template('email_template.txt')
    htmly = get_template('email_template.html')
    context = {'amount': amount, 'account_no': account_no, 'name': name, 'current_balance': current_balance}
    if transaction_type == 1:
        context['transaction_type'] = 'deposited to'
    else:
        context['transaction_type'] = 'withdrawn from'
    local_tz = pytz.timezone('Asia/Kolkata')
    context['date'] = date.replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%d %b %Y %I:%M:%S %p')
    text_content = plaintext.render(context)
    html_content = htmly.render(context)
    subject = 'Transaction Alert.'
    from_email = getattr(settings, "EMAIL_HOST_USER", None)
    try:
        msg = EmailMultiAlternatives(subject, text_content, from_email, [email])
        msg.attach_alternative(html_content, "text/html")
        response = msg.send()
        if not response:
            return False
        return True
    except Exception as e:
        print(e)
        return False
    