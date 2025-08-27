class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company
    
    def printDetails(self):
        print(f"Details for the {self.company}")
        print(f"Ticker:{self.ticker}\nPrice:{self.price}")
        print('\n')

apple = Stock(ticker="AAPL", price=150.00, company="Apple")
google = Stock(ticker="GOOGL", price=2800.00,company="Google")

apple.printDetails()
google.printDetails()

