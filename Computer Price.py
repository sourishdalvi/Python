class computer:
    def __init__(self, ):
        self.__Maxprice=900
    def sell(self):
        print("the price is {}",format(self.__Maxprice))
    def setMaxprice(self, price):
        self.__Maxprice=price
c=computer()
c.sell()
c.__Maxprice=1000
c.sell()
c.setMaxprice(1000)
c.sell()