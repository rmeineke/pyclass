import logging
import sys
import re
import os
import json
import account

# set up for logging
LEVELS = {'debug':logging.DEBUG,
          'info':logging.INFO,
          'warning':logging.WARNING,
          'error':logging.ERROR,
          'critical':logging.CRITICAL,
         }
if len(sys.argv) > 1:
    level_name = sys.argv[1]
    level = LEVELS.get(level_name, logging.NOTSET)
    logging.basicConfig(level=level)
    
    
def PromptForTransactionDate():
    '''
    ask the user for the date of this particular transaction
    '''
    while True:
        date = input("\nDate of transaction (mm/dd/yyyy): ")
        
        # make sure the date is proper format
        match = re.match('\d\d/\d\d/\d\d\d\d', date)
        if match:
            return date
        else:
            print("Bad date format ... use mm/dd/yyyy");


def PromptForTransactionDescription():
    '''
    need to have the specific type/description of
    the transaction ... append each line to a list
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
    dollars and cents ... e.g., 202.13
    '''
    amt = 0
    while True:
        amt = input('\nEnter amount of transaction: $')
        
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
        else:
            print('Bad amount format ... use ###.## ... for dollars and cents')
            
            
def CalculateQuarterShare(amt):
    '''
    calculate one quarter of the entire fee
    '''
    amt = int(amt * .25)
    return round(amt)
    
    
def CalculateMasterAccountShare(qtr_share, amt):
    '''
    separate calculation for the 'master' account 
    
    this needs to be calculated slightly differently
    as there may be a penny or two slop over based 
    upon money being divided four ways and then rounded
    '''
    non_master_ttl = 3 * qtr_share
    return amt - non_master_ttl
    
    
def GetDataFilePath():
    '''
    look in the "/Data" directory for the accounts file.
    return the full pathname ... or bomb out if not 
    found
    '''
    data_file = os.path.join('.', 'Data', 'accounts.json')
    if not os.path.exists(data_file):
        logger.critical('accounts file -{}- not found ... exiting'.format(data_file))
        exit()
    return data_file
    

def main():
    logger = logging.getLogger()
    logger.debug('Entering Main')
    
    DEBUG = 0
    if not DEBUG:
        date = PromptForTransactionDate()
        logger.debug('date: {}'.format(date))
        descr = PromptForTransactionDescription()
        logger.debug('descr: {}'.format(descr))
        amount = PromptForTransactionAmount()
        logger.debug('amount: {}'.format(amount))
    else:
        logger.debug('using test/debug input')
        date = '10/15/2016'
        descr = ['This test input', 'is a ', 'FOUR Line example', 'Testing ... dummy text']
        amount = 401.00


    # collect information from the user
    transaction_amount = int(float(amount) * 100)
    logger.debug('transaction_amount: {}'.format(transaction_amount))
    
    qtr_share = CalculateQuarterShare(transaction_amount)
    logger.debug('qtr_share: {}'.format(qtr_share))
    
    master_account_share = CalculateMasterAccountShare(qtr_share, transaction_amount)
    logger.debug('master_account_share: {}'.format(master_account_share))
    
    
    # now that the basic information has been gathered we'll
    # read the json file that contains the individual account
    # information ...
    
    data_file = GetDataFilePath()
    # open the file and read it in as json data
    with open(data_file) as data_file:
        data = json.load(data_file)

    # instantiate the account objects
    # then immediately call for the object to update itself
    accts = []
    for acct in data["accounts"]:
        acct_obj = account.Account(acct['address'], acct['name'], acct['reads_in'], acct['master'], os.path.join('.', 'Data', acct['file']))
        if acct_obj.master == 'no':
            acct_obj.WriteAdminFeeToAccountFile(date, qtr_share, descr)
        else:
            acct_obj.WriteAdminFeeToAccountFile(date, master_account_share, descr)
 
 
if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main()


'''
////// with test/debug data

[05:21] robertm -- /home/robertm/programming/pyclass/assignment5a $ python3 program.py debug
DEBUG:root:Entering Main
DEBUG:root:using test/debug input
DEBUG:root:transaction_amount: 40100
DEBUG:root:qtr_share: 10025
DEBUG:root:master_account_share: 10025
[05:21] robertm -- /home/robertm/programming/pyclass/assignment5a $ python3 program.py critical
[05:21] robertm -- /home/robertm/programming/pyclass/assignment5a $ 




////// interactive sessions

[05:22] robertm -- /home/robertm/programming/pyclass/assignment5a $ python3 program.py debug
DEBUG:root:Entering Main

Date of transaction (mm/dd/yyyy): dkfj
Bad date format ... use mm/dd/yyyy

Date of transaction (mm/dd/yyyy): djjdjdjdjd;
Bad date format ... use mm/dd/yyyy

Date of transaction (mm/dd/yyyy): 10/23/2016
DEBUG:root:date: 10/23/2016
Enter description ["q" to quit]: This is a test
Enter description ["q" to quit]: entry.
Enter description ["q" to quit]: q
DEBUG:root:descr: ['This is a test', 'entry.']
DEBUG:root:<class 'list'>

Enter amount of transaction: $kdfj
Bad amount format ... use ###.## ... for dollars and cents

Enter amount of transaction: $lsls
Bad amount format ... use ###.## ... for dollars and cents

Enter amount of transaction: $199.99
DEBUG:root:amount: 199.99
DEBUG:root:transaction_amount: 19999
DEBUG:root:qtr_share: 4999
DEBUG:root:master_account_share: 5002
[05:23] robertm -- /home/robertm/programming/pyclass/assignment5a $ python3 program.py critical

Date of transaction (mm/dd/yyyy): dkfj
Bad date format ... use mm/dd/yyyy

Date of transaction (mm/dd/yyyy): 10/24/2016
Enter description ["q" to quit]: Yearly well fee 
Enter description ["q" to quit]: To: Monterey County Health Dept.
Enter description ["q" to quit]: Paid by electr. funds xfer
Enter description ["q" to quit]: q

Enter amount of transaction: $dksfj
Bad amount format ... use ###.## ... for dollars and cents

Enter amount of transaction: $jdjd
Bad amount format ... use ###.## ... for dollars and cents

Enter amount of transaction: $199.99
[05:24] robertm -- /home/robertm/programming/pyclass/assignment5a $ 
[05:24] robertm -- /home/robertm/programming/pyclass/assignment5a $ python3 program.py critical

Date of transaction (mm/dd/yyyy): 10/25/2016
Enter description ["q" to quit]: Administrative test
Enter description ["q" to quit]: Three lines should be
Enter description ["q" to quit]: in the output
Enter description ["q" to quit]: q

Enter amount of transaction: $199.01
[05:26] robertm -- /home/robertm/programming/pyclass/assignment5a $ 


'''
