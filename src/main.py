from requestor.bithumb_requestor import BithumbRequestor


class Main:
    def __init__(self):
        self.bithumb_requestor = BithumbRequestor()

    def run_app(self):
        response = self.bithumb_requestor.get_market_codes()
        print(response.text)


main = Main()
main.run_app()