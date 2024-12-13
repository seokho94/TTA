from requestor.bithumb_requestor import BithumbRequestor


class Main:
    def __init__(self):
        self.bithumb_requestor = BithumbRequestor()

    def run_app(self):
        response_codes = self.bithumb_requestor.get_market_codes()
        print(response_codes.text)
        response_candle = self.bithumb_requestor.get_min_candles('KRW-BTC')
        print(response_candle.text)

main = Main()
main.run_app()