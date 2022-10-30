from admin import admin
class admin_operations:

    foodlist = []

    def add_food(self):
        print("      NEW FOOD    ")
        foodid = int(input("Enter food ID : "))
        name = input("Enter food name : ")
        quantity= input("Enter quantity : ")
        price= int(input(" price : "))
        discount = input("Enter discount : ")
        stock = input(" stock left: ")
        food_obj = admin(foodid,name,quantity,price,discount,stock)
        self.foodlist.append(food_obj)
        print("Successfully Added")

    def viewfood(self):
        print("*********fooditems*******")
        for food in self.foodlist:
            print(food,"\n")

    def search_food_by_ID(self,foodid):
        for food in self.foodlist:
            if food.get_foodid() == foodid:
                return food
        
        print("No such Book ID Found!!")
        return

    def delete_food(self):
        print(" Delete fooditem ")
        try:
            foodid = int(input("Enter food ID : "))
            food = self.search_food_by_ID(foodid)
            if food:
                self.foodlist.remove(food)
                print("Successfully Deleted")
        except Exception as invalid:
            print(invalid)

    def update_food(self):
        print("   Update food ")
        foodid = int(input("Enter food ID : "))
        food = self.search_food_by_ID(foodid)
        if food:
            foodid = int(input("Enter food ID : "))
            name = input("Enter name : ")
            quantity= input("Enter quantity: ")
            price= int(input("Enter price: "))
            discount = input("Enter discount: ")
            stock = input("Enter stock : ")

            admin.set_name(name)
            admin.set_quantity(quantity)
            admin.set_price(price)
            admin.set_discount(discount)
            admin.set_stock(stock)

            print("Successfully Updated")
