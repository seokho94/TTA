from libs.requestor.abstract_requestor import AbstractRequestor
import requests

class BithumbRequestor(AbstractRequestor):
    def get(url, headers={}, param={}):
        return requests.get(url, params=param, headers=headers)

    def post(url, param={}):
        requests.post(url, param)

    def put(url, param={}):
        requests.put(url, param)

    def delete(url, param={}):
        requests.delete(url, param)

    @staticmethod
    def get_market_codes(isDetail=False):
        url = "https://api.bithumb.com/v1/market/all"
        headers = {"accept": "application/json"}
        params = {'isDetail': isDetail}
        return BithumbRequestor.get(url, headers, params)