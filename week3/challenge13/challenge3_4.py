# -*- coding: utf-8 -*-

import re
from datetime import datetime
import pdb

def open_parser(filename):
    with open(filename) as logfile:
        pattern = (r''
                   r'(\d+.\d+.\d+.\d+)\s-\s-\s'
                   r'\[(.+)\]\s'
                   r'"GET\s(.+)\s\w+/.+"\s'
                   r'(\d+)\s'
                   r'(\d+)\s'
                   r'"(.+)"\s'
                   r'"(.+)"'
                   )
        parsers = re.findall(pattern,logfile.read())
    return parsers

def main():
    logs = open_parser('nginx.log')
    d = {}
    d2 = {}
    ip_dict = {}
    url_dict = {}
    for i in logs:
        if i[1][:11] == '11/Jan/2017':
            d.setdefault(i[0],0)
            d[i[0]] += 1
        if i[3] == '404':
            d2.setdefault(i[2],0)
            d2[i[2]] += 1

    l = sorted(d.values(), key=lambda x:-x)
    for k,v in d.items():
        if v == l[0]:
            ip_dict[k] = v
    l2 = sorted(d2.values(),key=lambda x:-x)
    for m,n in d2.items():
        if n == l2[0]:
            url_dict[m] = n


    return ip_dict,url_dict


if __name__ == '__main__':
    ip_dict,url_dict = main()
    print(ip_dict,url_dict)
