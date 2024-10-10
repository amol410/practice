class MenuItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Bill:
    def __init__(self, table_number, server_name):
        self.table_number = table_number
        self.server_name = server_name
        self.items = []
        self.gst_rate = 0.125

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        subtotal = sum(item.price for item in self.items)
        gst = subtotal * self.gst_rate
        total = subtotal + gst
        return subtotal, gst, total

    def print_bill(self):
        print(f"Table Number: {self.table_number}")
        print(f"Server: {self.server_name}")
        print("Items:")
        for item in self.items:
            print(f" - {item.name}: ${item.price:.2f}")
        subtotal, gst, total = self.calculate_total()
        print(f"Subtotal: ${subtotal:.2f}")
        print(f"GST (12.5%): ${gst:.2f}")
        print(f"Total: ${total:.2f}")

class Restaurant:
    def __init__(self):
        self.menu = []
        self.bills = []

    def add_menu_item(self, name, price):
        self.menu.append(MenuItem(name, price))

    def create_bill(self, table_number, server_name):
        bill = Bill(table_number, server_name)
        self.bills.append(bill)
        return bill

    def split_bill(self, bill, num_splits):
        split_bills = [Bill(bill.table_number, bill.server_name) for _ in range(num_splits)]
        for item in bill.items:
            split_price = item.price / num_splits
            for split_bill in split_bills:
                split_bill.add_item(MenuItem(item.name, split_price))
        
        return split_bills

# Example usage
restaurant = Restaurant()
restaurant.add_menu_item("Pasta", 12.00)
restaurant.add_menu_item("Pizza", 15.00)
restaurant.add_menu_item("Salad", 8.00)

# Create a bill for table 1
bill = restaurant.create_bill(1, "Alice")
bill.add_item(restaurant.menu[0])  # Pasta
bill.add_item(restaurant.menu[1])  # Pizza

# Print the bill
bill.print_bill()

# Split the bill into 2
split_bills = restaurant.split_bill(bill, 2)
for i, split_bill in enumerate(split_bills, start=1):
    print(f"\nSplit Bill {i}:")
    split_bill.print_bill()