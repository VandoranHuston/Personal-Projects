class User:

    def __init__(self, name, password, wishlist = None) -> None:
        self.name = name
        self.password = password
        self.wishlist = wishlist

    def getName(self) -> str:
        return self.name

    def getWishList(self) -> list:
        return self.wishlist
    
    def setPassword(self, password):
        self.password = password

    def addWish(self, shoe):
        self.wishlist.append(shoe)

    def removeShoes(self, shoe):
        index = self.wishlist.index(shoe)
        self.wishlist.pop(index)

def main():
    me = User("v", "h", ["b"])
    print(me.getWishList())
    me.removeShoes("b")
    print(me.getWishList())

if __name__ == "__main__":
    main()