#!/usr/bin/env python3
""" provides some status about Nginx logs stored in mongodb """
from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient()
    nginx_logs = client.logs.nginx.find()
    out = dict(logs=0,
               methods={'GET': 0, 'POST': 0,
                        'PUT': 0, 'PATCH': 0, 'DELETE': 0},
               status=0)

    # fille out the data
    for log in nginx_logs:
        out['logs'] += 1
        method = log.get('method')
        if method in out['methods']:
            out['methods'][method] += 1
        if log.get('path', None) == '/status':
            out['status'] += 1

    # print the data in the required format
    print(out['logs'], 'logs')
    print('Methods:')
    for k, v in out['methods'].items():
        print(f'\tmethod {k}: {v}')
    print(out['status'], 'status check')
