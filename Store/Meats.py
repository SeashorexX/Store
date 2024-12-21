class Meats:
    def __init__(self,meat,price):
        self.meat = meat
        self.price = price

m1 = ("1. Hamburger",5.00)
m2 = ("2. Turkey", 7.00)
m3 = ("3. Sausage", 3.00)
m4 = ("4. Hotdog", 4.00)
m5 = ("5. Bacon", 4.00)

meat_list = [m1,m2,m3,m4,m5]

print("\nInventory")
print("-----------")

def Show_meats():
    for meat in meat_list:
        print(f"{meat.meat}: ${meat.price:.2f}")

