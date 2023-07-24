class Shoe:

    def __init__(self, name, id, price, img):
        self.name = name
        self.id = id
        self.price = price
        self.img = img

    def getPrice(self):
        return self.price
    
    def getName(self):
        return self.name
    
    def getId(self):
        return self.id
    
    def getImg(self):
        return self.img