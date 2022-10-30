class admin():
    def __init__(self,foodid,name,quantity,price,discount,stock):
        self.__foodid=foodid
        self.__name=name
        self.__quantity=quantity
        self.__price=price
        self.__discount=discount
        self.__stock=stock

    def __str__(self):
        return f"food id:{self.__foodid} \nname:{self.__name} \nquantity:{self.__quantity} \nprice:{self.__price} \ndiscount:{self.__discount} \nstock:{self.__stock}"
        
    def set_foodid(self,foodid):
        self.__foodid = foodid

    def get_foodid(self):
        return self.__foodid

    def set_name(self,name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_quantity(self,quantity):
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def set_price(self,price):
        self.___price = price

    def get_price(self):
        return self.__price

    def set_discount(self,discount):
        self.__discount=discount

    def get_discount(self):
        return self.__discount

    def set_stock(self,stock):
        self.__stock=stock

    def get_stock(self):
        return self.__stock

if __name__ == "__main__":
    owner_obj= admin(1,"grill","full","410","10%",6)
    print(owner_obj)