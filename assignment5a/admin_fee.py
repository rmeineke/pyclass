import json
import os
import account
import re
import math


def main():
    DEBUG = 1
    if not DEBUG:
        date = prompt_for_transaction_date()
        descr = prompt_for_transaction_description()
        amount = prompt_for_transaction_amount()
    else:
        date = '08/15/2016'
        descr = 'This is a test'
        amount = 401.00
        
    amount = int(float(amount) * 100)
    qtr_share = calculate_qtr_share(amount)
    master_share = calculate_master_share(qtr_share, amount)
    data_file = get_data_file()
    
    # open the file and read it in as json data
    with open(data_file) as data_file:
        data = json.load(data_file)

    # instantiate the account objects and 
    # append them to a list of accounts
    accts = []
    for acct in data["accounts"]:
        #addr = acct['address']
        acct_data_file = os.path.join('.', 'Data', str(acct['address']) + '.well.txt')
        # print('data_file ... {}'.format(data_file))
        
        # open each file .... find the last balance in the account
        # should look like this ... 
        # 
        # 07/21/2016  -----  Jul 2016 Usage, Electric      $  14.28   $  65.77
        #
        # dollar sign
        # any number of characters
        # decimal point
        # 2 decimal characters (the 'cents')
        # any number of spaces
        # dollar sign
        # any number of characters
        # decimal point
        # 2 decimal characters (the 'cents')
        # the end of the string
        bal_regex = re.compile(r'\$.*.\d\d\s+\$(.*.\d\d)$') 
        last_bal = 0
        with open(acct_data_file) as acct_file:
            for line in acct_file:
                line = line.strip()
                mo = bal_regex.search(line)
                if mo:
                    # be sure to strip any spaces from the match
                    last_balance = mo.group(1).strip()
            print('{} /// {}'.format(last_balance, line))

        last_balance = int(float(last_balance) * 100)
        current_bal = 0
        if acct['master'] == 'yes':
            current_bal = int(float(last_balance) + master_share)
            amount_to_record = master_share
            print(' {} ... {} ... {}'.format(last_balance, master_share, current_bal))
        else:
            current_bal = int(float(last_balance) + qtr_share)
            amount_to_record = qtr_share
            print('last bal: {} ... qtr_share: {} ... current_bal: {}'.format(last_balance, qtr_share, current_bal))
        current_bal = int(current_bal * 100)
        print()
        
        # write out the information to each account file
        # print(acct)
        
        acct_obj = account.Account(acct['address'], acct['name'],
                    acct['reads_in'], acct['master'], data_file)
        
        acct_obj.WriteAdminFee(amount_to_record, descr, current_bal)
        
        #this may not be needed 
        #accts.append(acct_obj)
        
    

def calculate_qtr_share(amt):
    # 25%
    amt = int(amt * .25)
    return round(amt)
    
    
def calculate_master_share(qtr_share, amt):
    non_master_ttl = 3 * qtr_share
    return amt - non_master_ttl
    
    
def prompt_for_transaction_date():
    date = input("Date of transaction: ")
    
    # make sure the date is proper format
    match = re.match('\d\d/\d\d/\d\d\d\d', date)
    if match:
        return date
    else:
        print('date looks to be amiss . . . exiting')
        exit()
        

def prompt_for_transaction_description():
    # get the transaction info
    descr = []
    while True:
        resp = input('Enter description ["q" to quit]: ')
        if resp == 'q':
            break
        descr.append(resp)
    
    
def get_data_file():
    # get the data file and see if it exists
    data_file = os.path.join('.', 'Data', 'accounts.json' )
    if not os.path.exists(data_file):
        print("accounts file {} not found . . . exiting".format(data_file))
        exit()
    return data_file
    
    
def prompt_for_transaction_amount():
    
    amt = 0
    while True:
        amt = input('Enter amount of transaction: $')
        match = re.match('\d*\.\d\d', amt)
        #money = re.compile('|'.join([
          #r'^\$?(\d*\.\d{1,2})$',  # e.g., $.50, .50, $1.50, $.5, .5
          #r'^\$?(\d+)$',           # e.g., $500, $5, 500, 5
          #r'^\$(\d+\.?)$',         # e.g., $5.
        #]))
        if match:
            return amt    
            

if __name__ == '__main__':
    main()


'''
usage_ttls = 0
    sum_ttl = 0
    percents = 0
    for acct in accts:
        acct.set_usage()
        print('acct.usage ... \t\t{0:.2f}'.format(acct.usage))
        usage_ttls = usage_ttls + acct.usage
        print('acct.grand_ttl ... \t{0:.2f}'.format(acct.grand_ttl))
        sum_ttl = sum_ttl + acct.usage

        print('percentage used ... \t{0:.2f}'.format(acct.usage/acct.grand_ttl * 100))
        percents = percents + (acct.usage/acct.grand_ttl * 100)
        print()

    print('percents added ... \t{0:.2f}'.format(percents))
    print('usage_ttls ... \t\t{0:.2f}'.format(usage_ttls))
    print()
    print('sum_ttl ... \t\t{0:.2f}'.format(sum_ttl))
'''
