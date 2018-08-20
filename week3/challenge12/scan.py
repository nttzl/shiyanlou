# -*- coding utf-8 -*-

import sys,getopt
import socket

if len(sys.argv) != 5:
    print('Parameter Error')
    exit()
opts,args = getopt.getopt(sys.argv[1:],'h',['host=','port='])

for m, n in opts:
    if m in ('--host'):
        host = n
    if m in ('--port'):
        port = n

#print(host,port)
l2 = host.split('.')
if len(l2) != 4:
    print('Parameter Error')
    exit()

obj = socket.socket()
obj.settimeout(0.1)
l = port.split('-')
if len(l) == 1:
    try:
        obj.connect((host,int(port)))
        print('{} open'.format(port))
    except:
        print('{} closed'.format(port))
else:
    for i in range(int(l[0]),int(l[-1]) + 1):
        try:
            obj.connect((host,i))
            print('{} open'.format(i))
        except socket.error:
            print('{} closed'.format(i))

