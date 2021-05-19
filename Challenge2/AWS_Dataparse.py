import requests
import json
def load():
    awsurl = '<http://ipaddress/latest'

    awsmetadata = {'dynamic': {}, 'meta-data': {}, 'user-data': {}}
    for subsect in awsmetadata.keys():
        dataparse('{0}/{1}/'.format(awsurl, subsect), awsmetadata[subsect])
    return awsmetadata

def dataparse(url, data):
    res = requests.get(url)
    if res.status_code == 404:
        return
    for val in res.text.split('\n'):
        if not val:
            continue
        url1 = '{0}{1}'.format(url, val)
        if val.endswith('/'):
            key1 = val.split('/')[-2]
            data[key1] = {}
            dataparse(url1, data[key1])
        else:
            res = requests.get(url1)
            if res.status_code != 404:
                try:
                    data[val] = json.loads(res.text)
                except ValueError:
                    data[val] = r.text
            else:
                data[val] = None

if __name__ == '__main__':
    print(json.dumps(load()))