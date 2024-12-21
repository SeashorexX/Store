import math

title = "Shopping List Budget".center(120)
print(title)

categories = "Categories".center(120)
line = "------------".center(118)
print(categories, line)

cart = []


# Meats Class
class Meats:
    def __init__(self, meat, price):
        self.meat = meat
        self.price = price


meat_list = [
    Meats("1. Hamburger", 5.00),
    Meats("2. Turkey", 7.00),
    Meats("3. Sausage", 3.00),
    Meats("4. Hotdog", 4.00),
    Meats("5. Bacon", 4.00)
]

# Dairy Class
class Dairy:
    def __init__(self, dairy, price):
        self.dairy = dairy
        self.price = price


dairy_list = [
    Dairy("1. Milk", 3.00),
    Dairy("2. Butter", 2.50),
    Dairy("3. Cheese", 3.00),
    Dairy("4. Yogurt", 3.40),
    Dairy("5. Ice Cream", 4.00)
]

# Produce Class
class Produce:
    def __init__(self, produce, price):
        self.produce = produce
        self.price = price


produce_list = [
    Produce("1. Bananas", 4.00),
    Produce("2. Apples", 3.00),
    Produce("3. Grapes", 3.50),
    Produce("4. Strawberries", 4.20),
    Produce("5. Pineapples", 5.00)
]



# Snacks Class
class Snacks:
    def __init__(self, snacks, price):
        self.snacks = snacks
        self.price = price


snacks_list = [
    Snacks("1. Doritos", 2.00),
    Snacks("2. Fruit Snacks", 1.50),
    Snacks("3. Fruit Roll-Ups", 1.99),
    Snacks("4. Ruffles", 2.20),
    Snacks("5. Cheese Crackers", 1.00)
]


def Inventory(items):
    print("\nInventory")
    print("-----------\n")
    for item in items:
        print(
            f"{item.__class__.__name__}: {item.meat if hasattr(item, 'meat') else item.dairy if hasattr(item, 'dairy') else item.produce if hasattr(item, 'produce') else item.snacks}: ${item.price:.2f}"
        )
    print()


def calculate_total():
    return sum(item.price for item in cart)


def Cart(item):
    cart.append(item)
    print(
        f"\nAdded {item.meat if hasattr(item, 'meat') else item.dairy if hasattr(item, 'dairy') else item.produce if hasattr(item, 'produce') else item.snacks} to cart.\n"
    )


def show_category(category_items):
    while True:
        Inventory(category_items)
        choice = int(input("Select item number to add to cart (or 0 to go back): ")) - 1
        if choice == -1:
            break
        if 0 <= choice < len(category_items):
            Cart(category_items[choice])
        else:
            print("Invalid selection.")

def main():
    while True:
        print("\nWhich category would you like to shop from?: ")

        print("\n1. Meats")
        print("2. Dairy")
        print("3. Produce")
        print("4. Snacks")
        print("5. Checkout")

        try:
            choice = input("\nEnter your choice: ").lower()
            if choice == "meats":
                show_category(meat_list)
            elif choice == "dairy":
                show_category(dairy_list)
            elif choice == "produce":
                show_category(produce_list)
            elif choice == "snacks":
                show_category(snacks_list)
            elif choice == "checkout":
                print(f"\nTotal amount due: ${calculate_total():.2f}")
                print("\nThank you for shopping!\n")
                break
            else:
                print("\nInvalid Choice, please choose from the given categories.")
        except ValueError:
            print("Please enter a valid number.")


main()