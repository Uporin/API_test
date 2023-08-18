import requests
import json


class Run_Main(object):

    def send_get(self, url, data=None):
        response = requests.get(url=url, data=data)
        return json.dumps(response.json(), indent=2, sort_keys=False, ensure_ascii=False)

    def send_post(self, url, data, headers):
        response = requests.post(url=url, json=data, headers=headers)
        return json.dumps(response.json(), indent=2, sort_keys=False, ensure_ascii=False)

    def run_main(self, url, method, data=None, headers=None):
        result = None
        if method == 'GET':
            result = self.send_get(url, data)
        elif method == 'POST':
            result = self.send_post(url, data, headers)
        else:
            print("other method")

        return result


if __name__ == '__main__':
    run = Run_Main()