import logging
import re
import os
import json


def PromptForTransactionDate():
    '''
    ask the user for the date of this particular transaction
    '''
    while True:
        date = input("Date of transaction (mm/dd/yyyy): ")
        
        # make sure the date is proper format
        match = re.match('\d\d/\d\d/\d\d\d\d', date)
        if match:
            return date
        else:
            print("Bad date format ... use mm/dd/yyyy");


def PromptForTransactionDescription():
    '''
    need to have the specific type/description of
    the transaction
    '''
    descr = []
    while True:
        resp = input('Enter description ["q" to quit]: ')
        if resp == 'q':
            return descr
        descr.append(resp)
    

def PromptForTransactionAmount():
    '''
    looking for a dollar amount here
    '''
    amt = 0
    while True:
        amt = input('Enter amount of transaction: $')
        
        #here is a brain-dead regex that works for the moment
        match = re.match('\d*\.\d\d', amt)
        
        '''
        some other ideas to try later
        money = re.compile('|'.join([
          r'^\$?(\d*\.\d{1,2})$',  # e.g., $.50, .50, $1.50, $.5, .5
          r'^\$?(\d+)$',           # e.g., $500, $5, 500, 5
          r'^\$(\d+\.?)$',         # e.g., $5.
        ]))
        '''
        
        if match:
            return amt    
            
            

def CalculateQuarterShare(amt):
    '''
    25%
    one quarter of the entire bill
    '''
    amt = int(amt * .25)
    return round(amt)
    
    
def CalculateMasterAccountShare(qtr_share, amt):
    '''
    this needs to be calculated slightly differently
    as there may be a penny or two slop over based 
    upon money being divided four ways and then rounded
    '''
    non_master_ttl = 3 * qtr_share
    return amt - non_master_ttl
    
    
    
def GetDataFilePath():
    '''
    look in the "Data" directory for the accounts file.
    return the full pathname ... or bomb out if not 
    found
    '''
    data_file = os.path.join('.', 'Data', 'accounts.json' )
    if not os.path.exists(data_file):
        print("accounts file {} not found . . . exiting".format(data_file))
        exit()
    return data_file
    

def main():
    logger = logging.getLogger()
    logger.debug('Entering Main')
    
    DEBUG = 1
    if not DEBUG:
        date = PromptForTransactionDate()
        logger.debug('date: %s', date)
        descr = PromptForTransactionDescription()
        logger.debug('descr: %s', descr)
        amount = PromptForTransactionAmount()
        logger.debug('amount: %s', amount)
    else:
        date = '10/15/2016'
        descr = 'This is a test'
        amount = 401.00

    transaction_amount = int(float(amount) * 100)
    logger.debug('transaction_amount: %s', transaction_amount)
    
    qtr_share = CalculateQuarterShare(transaction_amount)
    logger.debug('qtr_share: %s', qtr_share)
    
    master_account_share = CalculateMasterAccountShare(qtr_share, transaction_amount)
    logger.debug('master_account_share: %s', master_account_share)
    
    # now that the basic information has been gathered we'll
    # read the json file that contains the individual account
    # information ...
    
    data_file = GetDataFilePath()
    # open the file and read it in as json data
    with open(data_file) as data_file:
        data = json.load(data_file)

    # instantiate the account objects and 
    # append them to a list of accounts
    accts = []
    for acct in data["accounts"]:
        acct_data_file = os.path.join('.', 'Data', str(acct['address']) + '.well.txt')
        logger.debug(acct_data_file)
        
        
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
        
        

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()
