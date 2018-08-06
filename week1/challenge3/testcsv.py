#!/usr/bin/env python3

import csv

a = '123412362454'
b = 7890
c = [123,456,789]
d = ['123','456','789']
e = ['nttzl','is','my','id']
g = [['this','is','the','first'],['second','list']] 

with open('1.csv','w',newline='') as f:
    csv.writer(f).writerows(g)

