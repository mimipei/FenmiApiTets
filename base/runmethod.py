import requests
import json


class RunMethod:
    def postMain(self, url, data, header=None):
        res = None
        if header != None:
            res = requests.post(url=url, data=data, headers=header)
        else:
            res = requests.post(url=url, data=data)
        return res.json()

    def getMain(self, url, data=None, header=None):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header, verify=False)
        else:
            res = requests.get(url=url, data=data, verify=False)
        return res.json()

    def runMain(self, method, url, data=None, header=None):
        res = None
        if method == 'Post':
            res = self.postMain(url, data, header)
        else:
            res = self.getMain(url, data, header)
        return json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)
