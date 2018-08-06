#!/usr/bin/env python3

def char_count_dict(str):
    l = {}
    for i in str:
        l[i] = str.count(i)
    for k,v in l.items():
        print('%s:,%d'%(k,v))

def char_count_set(str):
    char_list = set(str)
    for char in char_list:
        print(char,str.count(char))

def char_count_dict2(str):
    l = {}
    for i in str:
        if l.get(i) == None:
            l[i] = 1
        else:
            l[i] += 1
    for k,v in l.items():
        print('%s:%d'%(k,v))
            

if __name__ == '__main__':

    s = input("pleas input a str:")

    char_count_dict(s)
    char_count_set(s)
    char_count_dict2(s)
