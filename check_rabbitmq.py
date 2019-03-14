import json
from urllib import request

baseUrl = 'http://localhost:15672'
username = 'guest'
password = 'guest'

exchange_list = [
    'amq.direct',
    'amq.fanout',
    'test.exchange'
]
queue_list = [
    'test.ly34732',
    'demo'
]


def get_items(type):
    url = '{0}/api/{1}/{2}/'.format(baseUrl, type, '%2f')

    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, baseUrl, username, password)
    handler = request.HTTPBasicAuthHandler(password_mgr)
    req = request.Request(url)
    opener = request.build_opener(handler)

    res = opener.open(req).read().decode('utf-8', errors='ignore')
    items = [x['name'] for x in json.loads(res)]
    return set(items)

def check_alive():
    try:
        exchange_set = get_items('exchanges')
        queue_set = get_items('queues')

        print('Row, Type, Name, Status')
        # print exchange status
        for i, e in enumerate(exchange_list):
            print('{}, exchange, {}, {}'.format(
                i + 1,
                e,
                'OK' if e in exchange_set else 'Not Found'
            ))
        #print queue status
        for i, q in enumerate(queue_list):
            print('{}, queue, {}, {}'.format(
                i + len(exchange_list) + 1,
                q,
                'OK' if q in queue_set else 'Not Found'
            ))

    except Exception as ex:
        print('Row, Type, Name, Status')
        print('1, NA, NA, {}'.format(ex))


if __name__ == '__main__':
    check_alive()
