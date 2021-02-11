import pytz
def create_sheet(account, transactions, work_book):
    sheet_name = 'Account_'+str(account.account_no)
    worksheet = work_book.add_worksheet(sheet_name)
    if account.status == 2:
        worksheet.write('A1', 'Account Closed')
        worksheet.write('A2', 'Transaction ID')
        worksheet.write('B2', 'Datetime')
        worksheet.write('C2', 'Credit')
        worksheet.write('D2', 'Debit')
        worksheet.write('E2', 'Status')
        worksheet.write('F2', 'Remarks')
        row = 2
    else:
        worksheet.write('A1', 'Transaction ID')
        worksheet.write('B1', 'Datetime')
        worksheet.write('C1', 'Credit')
        worksheet.write('D1', 'Debit')
        worksheet.write('E1', 'Status')
        worksheet.write('F1', 'Remarks')
        row = 1
    local_tz = pytz.timezone('Asia/Kolkata')
    for transaction in transactions:
        date = transaction.transaction_time
        date = date.replace(tzinfo=pytz.utc).astimezone(local_tz).strftime('%d %b %Y %I:%M:%S %p')
        status = transaction.status
        if status == 1:
            status = 'Success'
        elif status == 2:
            status = 'Failed'
        else:
            status = 'Processing'
        col = 0
        transaction_row = [transaction.id, date, transaction.amount, status, transaction.remark]
        for elem in range(len(transaction_row)):
            if elem == 2 and transaction.type == 2:
                col += 1
            if elem == 3 and transaction.type == 1:
                col += 1
            worksheet.write(row, col, transaction_row[elem])
            col += 1
        row += 1
    return work_book