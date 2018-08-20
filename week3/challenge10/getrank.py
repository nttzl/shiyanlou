# -*- coding: utf-8 -*-
import sys
from pymongo import MongoClient


def get_rank(user_id):
        
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    dict1 = {}
    db = contests.find()
    for i in db:
        u = i['user_id']
        s = i['score']
        t = i['submit_time']
        if dict1.get(u):
            dict1[u][0] += int(s)
            dict1[u][1] += int(t)
        else:
            dict1[u] = [s,t]

    l = sorted(dict1.values(), key=lambda x:(-x[0],x[1]))

    for i,j in enumerate(l):
        for k,v in dict1.items():
            if v ==j:
                dict1[k].insert(0,i+1)
#        dict1[[k for k,v in dict1.items() if v == j][0]].insert(0,i+1)


    return tuple(dict1.get(int(user_id)))

if __name__ == '__main__':
    try:
        user_id = sys.argv[1]
        if len(sys.argv) != 2:
            raise IndexError()
    except IndexError:
        print('Parameter Error')
        exit()
    userdata = get_rank(user_id)
    print(userdata)
#    print(get_rank(2))
