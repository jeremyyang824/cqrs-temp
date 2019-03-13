import json
import sys
from urllib import request, error

baseUrl = 'http://localhost:15672'
username = 'guest'
password = 'guest'

def check_queue(quene_name):
    password_mgr = request.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, baseUrl, username, password)
    handler = request.HTTPBasicAuthHandler(password_mgr)

    req = request.Request(url=baseUrl + '/api/queues/%2f/' + quene_name)
    opener = request.build_opener(handler)

    try:
        res = opener.open(req).read().decode('utf-8', errors='ignore')
        obj = json.loads(res)
        return 'OK'
    except error.HTTPError as e:
        if e.code == 404:
            return 'Queue Not Found'
    except Exception as ex:
        return ex

if __name__ == '__main__':
    queue_name = sys.argv[1]
    print(check_queue(queue_name))
