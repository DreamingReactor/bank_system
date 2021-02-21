from trasactions.models import Transaction
from account.models import Account
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated
from trasactions.serializer import TransactionSerializer
import time
import xlsxwriter
from io import BytesIO
from django.http import HttpResponse
from trasactions.xls_creator import create_sheet
from trasactions.authenticate import ManagerAuthentication

class Withdraw(CreateAPIView):
    serializer_class = TransactionSerializer
    def post(self, request, **kwargs):
        account_obj = Account.objects.filter(account_no = request.data.get('account', ''))
        request.data['type'] = 2
        if not account_obj:
            request.data['account'] = None
        else:
            request.data['account'] = account_obj[0].pk
        response = super(Withdraw, self).post(request, **kwargs)
        return response

class Deposit(CreateAPIView):
    serializer_class = TransactionSerializer
    def post(self, request, **kwargs):
        account_obj = Account.objects.filter(account_no = request.data.get('account', ''))
        request.data['type'] = 1
        if not account_obj:
            request.data['account'] = None
        else:
            request.data['account'] = account_obj[0].pk
        response = super(Deposit, self).post(request, **kwargs)
        return response

class GenerateExcel(APIView):
    authentication_classes = (ManagerAuthentication,)
    permission_classes = (IsAuthenticated,)
    def post(self, request, **kwargs):
        account_list = request.data['account_list']
        transaction_status_type = request.data['transaction_status_type']
        manager_id = request.user
        xls_name = 'Trasaction_detail'+'_'+str(int(time.time()))+'_'+str(manager_id)+'.xlsx'
        output = BytesIO()
        work_book = xlsxwriter.Workbook(output)
        for account in account_list:
            if transaction_status_type == 'completed':
                status = 1
            elif transaction_status_type == 'failed':
                status = 2
            elif transaction_status_type == 'processing':
                status = 3
            else:
                status = None
            account_obj = Account.objects.filter(account_no = account)
            if account_obj:
                account_obj = account_obj[0]
                if status:
                    transactions = account_obj.transaction.filter(status = status)
                else:
                    transactions = account_obj.transaction.all()
                transactions.order_by('-transaction_time')
                work_book = create_sheet(account_obj, transactions, work_book)
        work_book.close()
        output.seek(0)
        response = HttpResponse(output.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
        response['Content-Disposition'] = "attachment; filename="+xls_name
        return response
