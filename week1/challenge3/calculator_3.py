#!/usr/bin/env python3
import sys
import csv

class Args:
    def __init__(self):
        
        l = sys.argv[1:]
        self.path_c = l[l.index('-c')+1]
        self.path_d = l[l.index('-d')+1]
        self.path_o = l[l.index('-o')+1]


class UserData(object):

    def __init__(self):
        self.userdata = self._read_users_data()

    def _read_users_data(self):
        list2 = []
        self.userdata = {}
        try:
            with open(args.path_d) as file:
                for line in file:
                    line = line.strip()
                    list2 = line.split(',')
                    self.userdata[int(list2[0])] = int(list2[1])
        except:
            print('Wrong user content')
            exit(-1)

        return self.userdata


class Config(object):
    def __init__(self):
        self.config = self._read_config()
    def _read_config(self):
        list1 = []
        d = {'s': 0}
        with open(args.path_c) as file:
            for line in file:
                line  = line.strip()
                list1 = line.split('=')
                a = list1[0].strip()
                b = list1[1].strip()    
                try:
                    if a == 'JiShuL' or a == 'JiShuH':
                        d[a] = float(b)
                    else:
                        d['s'] += float(b)
                except:
                    print('Wrong config content')
                    exit(-1)
        return d



class TaxCalculator(object):

    def __init__(self):
        self.result = []
        for id1,i in user.userdata.items(): 
            z = int(i)
            config = c.config
            shebao = z * config.get('s')
            if z < config.get('JiShuL'):
                shebao = config.get('JiShuL') * config.get('s')
            if z > config.get('JiShuH'):
                shebao = config.get('JiShuH') * config.get('s')
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
            self.result.append(['{},{},{:.2f},{:.2f},{:.2f}'.format(id1,z,shebao,shui,shuihou)])
#        print(self.result)
       
    def export(self):
        with open(args.path_o,'w') as f:
            writer = csv.writer(f)
#            for i in self.result:
#                f.write('{}\n'.format(i))
#                writer.writerow(str(i))
            writer.writerows(self.result)


if __name__ == '__main__':
    
    try:
        if len(sys.argv) != 7:
            raise ValueError()
    except ValueError:
        print('Parameter Error')
        exit(-1)
 
    args = Args()
    
    try:
        with open(args.path_c) as f:
            d = f.read()
        with open(args.path_d) as f:
            d = f.read()
    except FileNotFoundError:
        print("Wrong path!")
        exit(-1)

#    print(args.args)     
#    path = args.read_path()
    c = Config()     
#    print(config.config)
    user = UserData()
#    print(user.userdata)
    calc = TaxCalculator()
    calc.export()
