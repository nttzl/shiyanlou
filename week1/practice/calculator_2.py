#!/usr/bin/env python3
import sys

def calculate(**kw):
    for id1,salary in kw.items():
        insurance = salary * (0.08 + 0.02 + 0.005 + 0.06)
        TaxAmount = salary - insurance - 3500
        if TaxAmount < 0:
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
        after_tax = salary - insurance - tax
        print('{}:{:.2f}'.format(id1,after_tax))

if __name__ == '__main__':
    dict1 = {}
    list1 = sys.argv[1:]
    for i in list1:
        i.strip()
        list2 = i.split(':')
        str1 = list2[0]
        try:
            str2 = int(list2[1])
            if str2 < 0:
                raise ValueError()
        except ValueError:
            print("Parameter Error")
            break
        dict1[str1]=str2
    calculate(**dict1)
