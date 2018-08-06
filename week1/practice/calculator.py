#!/usr/bin/env python3

import sys

def calculate(num):
    TaxAmount = num - 3500
    if TaxAmount <= 1500:
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
    return tax


if __name__ == "__main__":
    try:
        if len(sys.argv) != 2:
            raise ValueError()
        else:
            num = int(sys.argv[1])
            if num < 0:
                raise ValueError()
            else:
                print("{:.2f}".format(calculate(num)))
    except ValueError:
        print("Parameter Error")
