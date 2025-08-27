class Stock:
    def __init__(self, ticker, price, company):
        self.ticker = ticker
        self.price = price
        self.company = company

    #For encapsulation we use getter setter and set price to internal use using _price
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

    
    def printDetails(self):
        print(f"Details for the {self.company}")
        print(f"Ticker:{self.ticker}\nPrice:{self.price}")
        print('\n')

    

apple = Stock(ticker="AAPL", price=150.00, company="Apple")
google = Stock(ticker="GOOGL", price=2800.00,company="Google")

apple.printDetails()
google.printDetails()