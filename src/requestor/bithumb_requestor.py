from asyncio.windows_events import NULL
from libs.requestor.abstract_requestor import AbstractRequestor
import requests

"""
Bithumb 거래소 Requestor
"""

class BithumbRequestor(AbstractRequestor):
    def get(url, headers={"accept": "application/json"}, params={}):
        return requests.get(url, params=params, headers=headers)

    def post(url, params={}):
        requests.post(url, params)

    def put(url, params={}):
        requests.put(url, params)

    def delete(url, params={}):
        requests.delete(url, params)

    """
    Bithum 마켓 코드 조회 Api
    Parameter
     (1) isDetail
      > Type: Boolean
      > Required: True
      > default: False
      > Desc: 상세 정보 조회 여부
    """
    @staticmethod
    def get_market_codes(isDetail=False):
        url = "https://api.bithumb.com/v1/market/all"
        params = {'isDetail': isDetail}
        return BithumbRequestor.get(url=url, params=params)

    """
    Bithum 분 단위 캔들 조회 Api
    Parameter
     (1) unit
      > Type: Integer
      > Required: True
      > Available: 1, 3, 5, 10, 15, 30, 60, 240
      > Desc: 기준 분 단위
     (2) market
      > Type: String
      > requried: True
      > Desc: 마켓 코드
      > ex) 'KRW-BTC'
     (3) to
      > Type: String
      > Required: False
      > Desc: 마지막 캔들 시각
      > ex) 2024-12-13 15:58:10  (yyyy-MM-dd HH:mm:ss)
     (4) count
      > Type: Integer
      > Required: Fasle
      > default: 1
      > Desc: 가져올 캔들 개수
      > Max: 200
    """
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
    
    """
    Bithum 일 단위 캔들 조회 Api
    Parameter
     (1) market
      > Type: String
      > requried: True
      > Desc: 마켓 코드 값
      > ex) 'KRW-BTC'
     (2) to
      > Type: String
      > Required: False
      > Desc: 마지막 캔들 시각
      > ex) 2024-12-13 15:58:10  (yyyy-MM-dd HH:mm:ss)
     (3) count
      > Type: Integer
      > Required: Fasle
      > default: 1
      > Desc: 가져올 캔들 개수
      > Max: 200
     (4) convertingPriceUnit
      > Type: String
      > Required: Fasle
      > Desc: 종가 환산 단위
      > ex) 'KRW'
    """
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
    
    """
    Bithum 주 단위 캔들 조회 Api
    Parameter
     (1) market
      > Type: String
      > requried: True
      > Desc: 마켓 코드 값
      > ex) 'KRW-BTC'
     (2) to
      > Type: String
      > Required: False
      > Desc: 마지막 캔들 시각
      > ex) 2024-12-13 15:58:10  (yyyy-MM-dd HH:mm:ss)
     (3) count
      > Type: Integer
      > Required: Fasle
      > default: 1
      > Desc: 가져올 캔들 개수
      > Max: 200
    """
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
    
    """
    Bithum 월 단위 캔들 조회 Api
    Parameter
     (1) market
      > Type: String
      > requried: True
      > Desc: 마켓 코드 값
      > ex) 'KRW-BTC'
     (2) to
      > Type: String
      > Required: False
      > Desc: 마지막 캔들 시각
      > ex) 2024-12-13 15:58:10  (yyyy-MM-dd HH:mm:ss)
     (3) count
      > Type: Integer
      > Required: Fasle
      > default: 1
      > Desc: 가져올 캔들 개수
      > Max: 200
    """
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