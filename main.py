print(" C2122-Homework-3-4 ")

class Customer:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def print_items(self):
        if self.items:
            print(f"{self.name} ordered the following items:")
            total = 0
            for item in self.items:
                print(f"\t{item.name}: {item.price} UAH")
                total += item.price
            print(f"Total: {total} UAH")
        else:
            print(f"{self.name} has no items ordered yet.")

class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Order:
    def __init__(self, order_number):
        self.order_number = order_number
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)

    def print_customers(self):
        if self.customers:
            print(f"Order {self.order_number} includes the following customers:")
            for customer in self.customers:
                print("\t", customer.name)
                customer.print_items()
        else:
            print(f"Order {self.order_number} has no customers yet.")

coffee = Item("Coffee", 50)
cake = Item("Cake", 80)
sandwich = Item("Sandwich", 120)

customer1 = Customer("Anton Grawskiy")
customer2 = Customer("Maksim Demerko")

customer1.add_item(coffee)
customer1.add_item(cake)

customer2.add_item(sandwich)
customer2.add_item(coffee)

order1 = Order(1)

order1.add_customer(customer1)
order1.add_customer(customer2)

order1.print_customers()