import json
import sys
from urllib import request, error

baseUrl = 'http://localhost:15672'
username = 'guest'
password = 'guest'

def check(url):
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, baseUrl, username, password)
    handler = request.HTTPBasicAuthHandler(password_mgr)
    req = request.Request(url)
    opener = request.build_opener(handler)

    try:
        res = opener.open(req).read().decode('utf-8', errors='ignore')
        obj = json.loads(res)
        return 'OK'
    except error.HTTPError as e:
        if e.code == 404:
            return 'Target Not Found'
    except Exception as ex:
        return ex

def check_exchange(exchange_name):
    url = baseUrl + '/api/exchanges/%2f/' + exchange_name
    return check(url)

def check_queue(quene_name):
    url = baseUrl + '/api/queues/%2f/' + quene_name
    return check(url)


if __name__ == '__main__':
    arg = sys.argv[1]
    item = sys.argv[2]
    if arg == '-e':
        print(check_exchange(item))
    elif arg == '-q':
        print(check_queue(item))
    else:
        raise Exception('arguments error.')
