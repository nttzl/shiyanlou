#!/usr/bin/env python3
import sys
import csv

class Config(object):

    def __init__(self):
        self.config = self._read_config()

    def _read_config(self):
        list1 = []
        self.config = {}
        with open(path[0]) as file:
            for line in file:
                line.strip()
                list1 = line.split('=')
                list1[0] = list1[0].strip()
                list1[1] = list1[1].strip()    
                self.config[list1[0]] = list1[1]
        return self.config



class UserData(object):

    def __init__(self):
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        list2 = []
        self.userdata = {}
        with open(path[1]) as file:
            for line in file:
                line = line.strip()
                list2 = line.split(',')
                self.userdata[list2[0]] = list2[1]
        return self.userdata




class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]
    
    def read_path(self):
        index_c = self.args.index('-c')
        self.path_c = self.args[index_c + 1]
        index_d = self.args.index('-d')
        self.path_d = self.args[index_d + 1]
        index_o = self.args.index('-o')
        self.path_o = self.args[index_o + 1]
        return self.path_c,self.path_d,self.path_o

class TaxCalculator(object):
    
    def calc_for_all_userdata(self):
        dict1 = config.config
#        print(dict1['YangLao'])
#        shebaolv = 0.1
        shebaolv = float(dict1['YangLao']) + float(dict1['YiLiao']) + float(dict1['ShiYe']) + float(dict1['GongJiJin'])
        JiShul = float(dict1['JiShuL'])
        JiShuh = float(dict1['JiShuH'])

        result = []
        for id1, salary in user.userdata.items():
            salary = int(salary)
            if salary < JiShul:
                shebao = shebaolv * JiShul
            elif salary > JiShuh:
                shebao = shebaolv * JiShuh
            else:
                shebao = shebaolv * salary

            TaxAmount = salary - shebao -3500
            if TaxAmount < 0:
                TaxAmount = 0
                TaxRate = 0
                deduction = 0
            elif TaxAmount <= 1500:
                TaxRate = 0.03
                deduction = 0
            elif TaxAmount <= 4500:
                TaxRate = 0.1
                deduction = 105
            elif TaxAmount <=9000:
                TaxRate = 0.2
                deduction = 555
            elif TaxAmount <= 35000:
                TaxRate = 0.25
                deduction = 1005
            elif TaxAmount <= 55000:
                TaxRate = 0.3
                deduction = 2755
            elif TaxAmount <= 80000:
                TaxRate = 0.35
                deduction = 5505
            else:
                TaxRate = 0.45
                deduction = 13505
            tax = TaxAmount*TaxRate - deduction    
            after_tax = salary - shebao - tax
            result.append(('{},{},{:.2f},{:.2f},{:.2f}'.format(id1,salary,shebao,tax,after_tax))) 
#            print('{},{},{:.2f},{:.2f},{:.2f}'.format(id1,salary,shebao,tax,after_tax))
        return result


    def export(self, default='csv'):
        result = self.calc_for_all_userdata()
#        print(result)
        with open(path[2],'w') as f:
#            writer = csv.writer(f)
            for i in result:
                f.write('{}\n'.format(i))
#                writer.writerow((str(i)))
#            writer.writerows(result)


if __name__ == '__main__':
    args = Args()
#    print(args.args)     
    path = args.read_path()
    config = Config()
#    print(config.config)
    user = UserData()
#    print(user.userdata)
    calc = TaxCalculator()
    calc.export()
