# bank_system

__python version: 3.8.5__

__OS: Ubuntu 20.04__

## Setting up project

### Run following command in terminal:

* $ git clone https://github.com/DreamingReactor/bank_system.git
* $ sudo apt update
* $ sudo apt install redis-server
* $ sudo apt install python3-venv
* $ python3 -m venv project_env_name
* $ source project_env_name/bin/activate
* $ cd bank_system
* $ pip install wheel
* $ pip install -r requirements.txt

Last command will install required packages in environment. After packages are installed run following command:

* $ python manage.py makemigrations
* $ python manage.py migrate
* $ python manage.py createsuperuser.(This will prompt you to enter user details, for creation of super user.)
* $ python manage.py runserver.(Starts up local server at default address http://127.0.0.1:8000)

Go to http://127.0.0.1:8000/admin on a webbrowser and login with super user credential. This will open up django admin panel, which can be used to enter rows in tables.(Account, Trasaction, User)

Switch back to terminal and use Ctrl+C to exit from running server. In terminal, use following commands to create a user, which will be used for calling Excel Sheet generation API.

    $ python manage.py shell
        >>from create_user import create_user
        >>create_user('username', 'password')

Press Ctrl+D to exit. 

__NOTE: To enable email notification, set appropriate email credentials against EMAIL_HOST_USER and EMAIL_HOST_PASSWORD in bank_system/bank_system/settings.py.__

__NOTE: General account password for google won't work if 2-step verification is enabled. App password would've to be generated from account's security settings.__

Start server again. 

Open new terminal tab and enter following command.
> $ celery -A bank_system worker -l info

This will starts a celery worker, in which Withdraw and Deposit tasks are queued.

Use any API client, like Postman, to make API requests.

## API Details

__Base URL: http://127.0.0.1:8000__


### For getting account balance

__URL pattern: /account/check_balance/\<int:account_no\>__

__Method: GET__

__Sample Response:__
> {"account_no":1,"balance_amount":109000.0}


### For depositing money

__URL pattern: /transaction/deposit__

__Method: POST__

__Content-Type: application/json__

__JSON Field:__

    amount: Amount to be deposited.
    account: Account number of account in which amount is to be deposited.

__Sample Request Body:__
> {"amount": 10000, "account": 1}

__Sample Response:__
> {"success":true,"message":"Transaction successful"}


### For with withdrawing money

__URL pattern: /transaction/withdraw__

__Method: POST__

__Content-Type: application/json__

__JSON Field:__

    amount: Amount to be withdrawn.
    account: Account number of account in which amount is to be deposited.

__Sample Request Body:__
> {"amount": 10000, "account": 1}

__Sample Response:__
> {"success":true,"message":"Transaction successful"}


### For generating excel sheet of trasaction for given user.

__URL pattern: /transaction/generate_xl__

__Method: POST__

__Content-Type: application/json__

__JSON Field:__
    
    account_list: List of accounts for which excel file has to be generated. Transaction detail of each account in the list will be saved in seprate sheet within the file. 
    
    transaction_status_type: To filter on trasaction status(Successful, Failed or Processing). Following values are accepted:
        null(default): All transaction.        
        completed: Will get only successful transaction.
        failed: Will get only failed transaction
        processing: Will get transaction which are still processing.
    
    username: Username of User previously created in python shell.
    
    password: Password of User previously created in python shell.

__Sample Request Body:__
> {"account_list": [1], "transaction_status_type": null, "username": "username", "password": "password"}

__Response:__
> A file which has to be saved as .xlsx file.

## Further Development

* Setting up task queues to process write APIs.(Done)
