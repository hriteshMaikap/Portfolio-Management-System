from abc import ABC, abstractmethod

class Asset(ABC):
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

    @abstractmethod
    def get_description(self):
        """Return description of the asset"""
        pass

class Stock(Asset):
    """Sub Class that inherits Asset"""
    def __init__(self, ticker, price, company):
        super().__init__(price)
        self.ticker = ticker
        self.company = company

    def get_description(self):
        res = f"Company Name: {self.company}\nTicker: {self.ticker}\nPrice: {self.price}\n"
        return res

class Bond(Asset):
    def __init__(self, price, interest_rate, maturity_date):
        super().__init__(price)
        self.interest_rate = interest_rate
        self.maturity_date = maturity_date
    
    def get_description(self):
        res = f"Price:{self.price}\nInterest Rate:{self.interest_rate}\nMaturity Date:{self.maturity_date}\n"
        return res
    
apple = Stock(ticker="AAPL", price=150.00, company="Apple")
google = Stock(ticker="GOOGL", price=2800.00,company="Google")
hinduja_limited = Bond(price=1000.00,interest_rate=15,maturity_date="1 January 2026")

portfolio = [apple, hinduja_limited]

for item in portfolio:
   if type(item) is Bond:
       print("Bond")
   if type(item) is Stock:
       print("Stock")
   print(item.get_description())
