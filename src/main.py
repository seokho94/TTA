from requestor.bithumb_requestor import BithumbRequestor


class Main:
    def __init__(self):
        self.bithumb_requestor = BithumbRequestor()

    def run_app(self):
        self.bithumb_requestor.test()


main = Main()
main.run_app()