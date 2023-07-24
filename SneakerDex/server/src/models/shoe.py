class Shoe:

    def __init__(self, name, id, price):
        self.name = name
        self.id = id
        self.price = price

    def getPrice(self):
        return self.price
    
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id