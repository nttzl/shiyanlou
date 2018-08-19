# -*- coding: utf-8 -*-

import sys
from pymongo import MongoClient
import pdb

def get_rank(user_id):
    client = MongoClient()
    db = client.shiyanlou
    contests = db.contests

    d = contests.find({'user_id':user_id})
    score = 0
    submit_time = 0
    for i in d:
        pdb.set_trace()
        score += int(i['score'])
        submit_time += int(i['submit_time'])

    return score, submit_time

if __name__ == '__main__':
    try:
        user_id = sys.argv[1]
        if len(sys.argv) != 2:
            raise ValueError()
    except ValueError:
        print('Parameter Error')
        exit()
    userdata = get_rank(user_id)
    print(userdata)
