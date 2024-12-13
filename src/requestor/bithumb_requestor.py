from libs.requestor.abstract_requestor import AbstractRequestor
import requests

class BithumbRequestor(AbstractRequestor):
    def get(url, param={}):
        requests.get(url)

    def post(url, param={}):
        requests.post(url, param)

    def put(url, param={}):
        requests.put(url, param)

    def delete(url, param={}):
        requests.delete(url, param)

    @staticmethod
    def test():
        print('test code')