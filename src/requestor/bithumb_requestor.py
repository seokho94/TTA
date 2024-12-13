from asyncio.windows_events import NULL
from libs.requestor.abstract_requestor import AbstractRequestor
import requests

class BithumbRequestor(AbstractRequestor):
    def get(url, headers={"accept": "application/json"}, params={}):
        return requests.get(url, params=params, headers=headers)

    def post(url, params={}):
        requests.post(url, params)

    def put(url, params={}):
        requests.put(url, params)

    def delete(url, params={}):
        requests.delete(url, params)

    @staticmethod
    def get_market_codes(isDetail=False):
        url = "https://api.bithumb.com/v1/market/all"
        params = {'isDetail': isDetail}
        return BithumbRequestor.get(url=url, params=params)
    
    @staticmethod
    def get_min_candles(market, to=None, count=1, unit=1):
        #market: String, to: String, count: Integer
        url = f"https://api.bithumb.com/v1/candles/minutes/{unit}"
        params = {
            "market": market,
            "to": to,
            "count": count
        }

        remove_none = {k: v for k, v in params.items() if v is not None}

        return BithumbRequestor.get(url=url, params=remove_none)
    
    @staticmethod
    def get_day_candles(market, to=None, count=1, convertingPriceUnit=None):
        url = "https://api.bithumb.com/v1/candles/days"
        params = {
            "market": market,
            "to": to,
            "count": count,
            "convertingPriceUnit": convertingPriceUnit
        }
        
        remove_none = {k: v for k, v in params.items() if v is not None}

        return BithumbRequestor.get(url=url, params=remove_none)
    
    @staticmethod
    def get_week_candles(market, to=None, count=1):
        url = "https://api.bithumb.com/v1/candles/weeks"
        params = {
            "market": market,
            "to": to,
            "count": count
        }

        remove_none = {k: v for k, v in params.items() if v is not None}
        
        return BithumbRequestor.get(url=url, params=remove_none)
    
    @staticmethod
    def get_month_candles(market, to=None, count=1):
        url = "https://api.bithumb.com/v1/candles/months"
        params = {
            "market": market,
            "to": to,
            "count": count
        }

        remove_none = {k: v for k, v in params.items() if v is not None}

        return BithumbRequestor.get(url=url, params=remove_none)