#!/usr/bin/env python3
import sys,csv,getopt,configparser
from multiprocessing import Queue,Process
import pdb
from datetime import datetime

def handle_args():
    try:
        opts,args = getopt.getopt(sys.argv[1:],'hC:c:d:o:',['help'])
    except getopt.GetoptError:
        print('getopterror')
        sys.exit()
#    pdb.set_trace()
    global cityname,configfile,userdatafile,outputfile
    cityname = 'DEFAULT'

    for name,value in opts:
        if name in ('-h','--help'):
            print('Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata')
#        if name in ('-c'&'-d'&'-o'):   #canshu xianzhi
#            continue
#        else:
#            exit(-1)
        if name in ('-C'):
            cityname = value.upper()
        if name in ('-c'):
            configfile = value
        if name in ('-d'):
            userdatafile = value
        if name in ('-o'):
            outputfile = value

def read_config():
    config = configparser.ConfigParser()
    config.read(configfile)
    global jishul,jishuh,shebaolv
    shebaolv = 0
    for k,v in config.items(cityname):
#        pdb.set_trace()
        if k == 'jishul':
            jishul = float(v)
        if k == 'jishuh':
            jishuh = float(v)
        if k != 'jishul' and k != 'jishuh':
            shebaolv += float(v)
#    pdb.set_trace()


def read_userdata(q1):
    list2 = []
    userdata = {}
    try:
        with open(userdatafile) as file:
            for line in file:
                line = line.strip()
                list2 = line.split(',')
                userdata[int(list2[0])] = int(list2[1])
    except:
        print('Wrong user content')
        exit(-1)
    q1.put(userdata)




def calc_data(q1,q2):
    newdata = []
    data = q1.get()

    for id1,i in data.items(): 
        z = int(i)
        shebao = z * shebaolv
        if z < jishul: 
            shebao = jishul * shebaolv
        if z > jishuh: 
            shebao = jishuh * shebaolv 
        x = z - shebao - 3500
        if x <= 0:
            shui = 0
        elif x <= 1500:
            shui = x * 0.03
        elif x <= 4500:
            shui = x * 0.1 - 105
        elif x <= 9000:
            shui = x * 0.2 - 555
        elif x <= 35000:
            shui = x * 0.25 -1005
        elif x <= 55000:
            shui = x * 0.3 - 2750
        elif x <= 80000:
            shui = x * 0.35 - 5505
        else:
            shui = x * 0.45 - 13505
        shuihou = z - shebao - shui
        t = datetime.now()
        time = datetime.strftime(t,'%Y-%m-%d %H:%M:%S')
        newdata.append(['{},{},{:.2f},{:.2f},{:.2f},{}'.format(id1,z,shebao,shui,shuihou,time)])
        q2.put(newdata)


def export(q2):
    result = q2.get()
    with open(outputfile,'w') as f:
        writer = csv.writer(f)
        writer.writerows(result)


if __name__ == '__main__':
    
    handle_args() 
    read_config() 

    
    q1=Queue()
    q2=Queue()
    p1 = Process(target=read_userdata, args=(q1,))
    p2 = Process(target=calc_data, args=(q1,q2))
    p3 = Process(target=export, args=(q2,))
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
