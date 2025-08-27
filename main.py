class Asset:
    """Parent Class"""
    def __init__(self, price):
        self.price = price
    
    @property
    def price(self):
        """The getter method for internal _price"""
        return self._price
    
    @price.setter
    def price(self, value):
        """Validates the data before modification"""
        if value<0:
            raise ValueError("Price cannot be negative")
        self._price=value

class Stock(Asset):
    """Sub Class that inherits Asset"""
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def printDetails(self):
        print(f"Details for the {self.company}")
        print(f"Ticker:{self.ticker}\nPrice:{self.price}")
        print('\n')

    

apple = Stock(ticker="AAPL", price=150.00, company="Apple")

google = Stock(ticker="GOOGL", price=2800.00,company="Google")

apple.printDetails()
google.printDetails()