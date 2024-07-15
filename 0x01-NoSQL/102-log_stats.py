#!/usr/bin/env python3
"""
This script retrieves and prints statistics from a MongoDB collection of logs.
"""

from pymongo import MongoClient


if __name__ == '__main__':
    client = MongoClient()
    logs = client.logs.nginx
    out = dict(logs=logs.count_documents({}),
               methods={'GET': logs.count_documents({'method': 'GET'}),
                        'POST': logs.count_documents({'method': 'POST'}),
                        'PUT': logs.count_documents({'method': 'PUT'}),
                        'PATCH': logs.count_documents({'method': 'PATCH'}),
                        'DELETE': logs.count_documents({'method': 'DELETE'})},
               status=logs.count_documents({'method': 'GET',
                                            'path': '/status'}),
               ips=logs.aggregate([
                    {
                        "$group": {
                            "_id": "$ip",
                            "total": {"$sum": 1}
                        }
                    },
                    {
                        "$sort": {
                            "total": -1,
                            "_id": -1
                        }
                    },
                    {
                        "$limit": 10
                    }
                ])
               )

    # print the data in the required format
    print(out['logs'], 'logs')
    print('Methods:')
    for k, v in out['methods'].items():
        print(f'\tmethod {k}: {v}')
    print(out['status'], 'status check')
    print('IPs:')
    for ip in out['ips']:
        print(f'\t{ip.get('_id')}: {ip.get('total')}')
