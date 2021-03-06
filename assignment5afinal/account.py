'''
This account.py module houses the Account class 
and any account-related functionality
'''

class Account:
    '''
    The Account class is populated once the main
    program is run. All data is retrieved from the 
    master account list which is in a JSON file in 
    the /Data directory that should sit under the
    current working directory
    '''
    
    def __init__(self, address, name, reads_in, master, datafile):
        self.address = address
        self.name = name
        self.readsin = reads_in
        self.master = master
        self.datafile = datafile
        
        # this will 'self-fire' a function
        # that retrieves and initializes the current 
        # account balance for this particular account object
        self.SetCurrentBalance()
    

    def __str__(self):
        return """
        name: %(name)s
        addr: %(address)s
        reads in: %(readsin)s
        master?: %(master)s
        file: %(datafile)s
        bal: %(current_balance)s
        """ % self.__dict__
    
    def SetCurrentBalance(self):
        '''
        Parse each account data file and retrieve the 
        account's current balance ... then set the 
        object's balance property
        
        This function is self-fired when the object is first
        initialized ... see the __init__
        '''
        with open(self.datafile) as acct_file:
            backwards_lines = acct_file.readlines()
            backwards_lines.reverse()
            for line in backwards_lines:
                if line.count("$") != 2:
                     continue
                parts = line.split()
                if parts[-2] != '$' or parts[-4] != '$':
                    continue
                break           
            self.current_balance = int(float(parts[-1]) * 100)

          
    def WriteAdminFeeToAccountFile(self, date, amount, transaction_details):
        '''
        Append the fee information to the account object's data file
        '''
        
        # open file and append the transaction to the end
        with open(self.datafile, 'a') as acct_file:
            # first line of transaction detail
            acct_file.write('\n{}  -----  {:30}${:7.2f}   ${:7.2f}\n'. \
                        format(date, transaction_details[0], (amount/100), \
                        ((self.current_balance + amount)/100)))
            
            # remaining lines of the transaction detail            
            for line in transaction_details[1:]:
                    acct_file.write('                   {}\n'.format(line))
            
        
        # legacy perl code ... for example output spacing
        """
        printf {$OUT} "%s  -----  $mo $yr Usage, Electric      \$%7.2f   \$%7.2f\n",
        $self->get_date_last_read(), $self->get_bill(), $self->get_bal();
        """
