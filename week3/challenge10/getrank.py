# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient
import pdb

client = MongoClient()
db = client.shiyanlou
contests = db.contests

dict1 = {}
db = contests.find()
for i in db:
    get = dict1.get(i['user_id'])
    if get is None:
        dict1[i['user_id']] = {'score':int(i['score']),'time':int(i['submit_time'])}
    else:
        dict1[i['user_id']]['score'] = get.get('score') + int(i['score']) 
        dict1[i['user_id']]['time'] = get.get('time') + int(i['submit_time']) 
print(dict1.values())
s = sorted(dict1.items(), key = lambda x: x[1])
print(s)

def get_rank(user_id):
    

    return score, submit_time

if __name__ == '__main__':
    try:
        user_id = sys.argv[1]
        if len(sys.argv) != 2:
            raise IndexError()
    except IndexError:
        print('Parameter Error')
        exit()
    print
    userdata = get_rank(user_id)
    print(userdata)
#    print(get_rank(2))
