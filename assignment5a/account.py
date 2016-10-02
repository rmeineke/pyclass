# account class 
import re
import numpy

class Account:
    def __init__(self, address, name, reads_in, master, datafile):
        self.address = address
        self.name = name
        self.readsin = reads_in
        self.master = master
        self.datafile = datafile


    def WriteAdminFee(self, amount, transaction_detail, current_balance):
        print()
        print('WriteAdminFee: {} ... {} ... {}'.format(amount, transaction_detail, current_balance))

        
    def set_usage(self):
        usage_list = []
        ttl_usage_list = []
        with open(self.datafile) as acct_file:
            for line in acct_file:
                
                # loop through the data files and look for 
                # 1/ usage lines
                # 2/ total well usage lines
                match = re.match(r'Usage \(gallons\)\s*(\d+.\d\d)', line)
                match2 = re.match(r'Total well usage \(gallons\)\s*(\d+.\d\d)', line)
                
                #if anything is found .... append it to the appropriate list
                if match:
                    usage_list.append(float(match.group(1)))
                    # print(line, end='')

                if match2:
                    ttl_usage_list.append(float(match2.group(1)))
                    # print(line, end='')

            # calculate total, individual usage
            ttl_used = 0
            truncated_list = usage_list[-12:]
            for num in truncated_list:
                ttl_used = ttl_used + num
            print('ttl_used ... \t\t{0:.2f}'.format(ttl_used))

            # calculate total, group usage
            grand_ttl = 0
            last_twelve_ttl_usage = ttl_usage_list[-12:]
            for num in last_twelve_ttl_usage:
                grand_ttl = grand_ttl + num

            self.usage = ttl_used
            self.grand_ttl = grand_ttl
