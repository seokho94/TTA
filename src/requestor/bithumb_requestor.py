from asyncio.windows_events import NULL
from libs.requestor.abstract_requestor import AbstractRequestor
import requests

class BithumbRequestor(AbstractRequestor):
    def get(url, headers={"accept": "application/json"}, param={}):
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
        params = {'isDetail': isDetail}
        return BithumbRequestor.get(url=url, param=params)
    
    @staticmethod
    def get_min_candles(market, to=NULL, count=1, unit=1):
        #market: String, to: String, count: Integer
        url= f"https://api.bithumb.com/v1/candles/minutes/{unit}"
        params = {
            "market": market,
            "count": count
        }

        if(to != NULL):
            params.to = to

        return BithumbRequestor.get(url=url, param=params)
        