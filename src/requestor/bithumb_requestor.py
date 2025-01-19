from pdb import runcall
from sqlite3 import paramstyle
from libs.requestor.abstract_requestor import AbstractRequestor
import requests

from util.authorization import Autorization


"""
Bithumb 거래소 Requestor

PUBLIC API
"""
class BithumbRequestor(AbstractRequestor):
    @staticmethod
    def get(url, headers={"accept": "application/json"}, params={}):
        return requests.get(url, params=params, headers=headers)

    @staticmethod
    def post(url, params={}):
        return requests.post(url, data=params)

    @staticmethod
    def put(url, params={}):
        return requests.put(url, data=params)

    @staticmethod
    def delete(url, params={}):
        return requests.delete(url, params=params)

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
    def get_market_codes(isDetail=None):
        url = "https://api.bithumb.com/v1/market/all"
        params = {'isDetail': isDetail}
        remove_none = {k: v for k, v in params.items() if v is not None}
        return BithumbRequestor.get(url=url, params=remove_none)

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
    def get_min_candles(market, to=None, count=None, unit=1):
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
    def get_day_candles(market, to=None, count=None, convertingPriceUnit=None):
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
    def get_week_candles(market, to=None, count=None):
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
    def get_month_candles(market, to=None, count=None):
        url = "https://api.bithumb.com/v1/candles/months"
        params = {
            "market": market,
            "to": to,
            "count": count
        }

        remove_none = {k: v for k, v in params.items() if v is not None}

        return BithumbRequestor.get(url=url, params=remove_none)
    
    """
    Bithum 최근 체결 내역 조회 Api
    Parameter
     (1) market
      > Type: String
      > requried: True
      > Desc: 마켓 코드 값
      > ex) 'KRW-BTC'
     (2) to
      > Type: String
      > Required: False
      > Desc: 마지막 체결 시각
      > ex) 15:58:10 or 155810  (HH:mm:ss or HHmmss)
     (3) count
      > Type: Integer
      > Required: Fasle
      > default: 1
      > Desc: 체결 개수
     (4) cursor
      > Type: String
      > Required: Fasle
      > Desc: 페이지네이션 커서
     (5) daysAgo
      > Type: Int32
      > Required: Fasle
      > Desc: 최근 7일 이내의 이전 데이터 조회
      > available: 1, 2, ,3, 4, 5, 6, 7 
    """
    @staticmethod
    def get_trade_ticks(market, to=None, count=None, cursor=None, daysAgo=None):
        url="https://api.bithumb.com/v1/trades/ticks"
        params = {
            "market": market,
            "to": to,
            "count": count,
            "cursor": cursor,
            "daysAgo": daysAgo
        }

        remove_none = {k: v for k, v in params.items() if v is not None}

        return BithumbRequestor.get(url=url, params=remove_none)
    
    """
    Bithum 현재가 정보 조회 Api
    Parameter
     (1) markets
      > Type: String
      > Required: True
      > default: False
      > Desc: 마켓 코드, 여러 코인 조회 시 반점으로 구분
      > ex) KRW-BTC,KRW-XRP,KRW-ETH
    """
    @staticmethod
    def get_current_price(markets):
        url = "https://api.bithumb.com/v1/ticker"
        params = { "markets": markets }

        return BithumbRequestor.get(url=url, params=params)
    
    @staticmethod
    def get_ticker_info(markets):
        url = "https://api.bithumb.com/v1/orderbook"
        params = { "markets": markets }

        return BithumbRequestor.get(url=url, params=params)
    
    @staticmethod
    def get_warning_info():
        url = "https://api.bithumb.com/v1/market/virtual_asset_warning"

        return BithumbRequestor.get(url=url)
    
    """
Bithumb 거래소 Requestor

PRIVATE API
"""
    @staticmethod
    def get_all_accounts():
        url = "https://api.bithumb.com/v1/accounts"
        
        authorization_token = Autorization.make_jwt_token('bithumb')
        
        print(authorization_token)
        headers = { "Authorization": authorization_token }

        return BithumbRequestor.get(url=url, headers=headers)