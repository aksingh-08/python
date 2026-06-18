from collections import defaultdict, Counter
import time 

class InventorySystem:
    def __init__(self):
        self.inventory = {}
        self.categories = defaultdict(list)
        self.sales_counter = Counter()
        self.item_ids = set()

    def add_tem(self, item_id, name, category, quantity):
        if item_id in self.item_ids:
            raise ValueError("Item ID already exists")
        item_data = {
            "name": name, 
            "category": category,
            "quantity": quantity
        }
        self.inventory[item_id] = item_data
        self.categories[category].append(item_id)
        self.item_ids.add(item_id)

    def remove_item(self, item_id):
        if item_id not in self.item_ids:
            raise ValueError("Item does not exist")

        category = self.inventory[item_id]["category"]

        del self.inventory[item_id]
        self.categories[category].remove(item_id)
        self.item_ids.remove(item_id)

    def update_stock(self, item_id, quantity):
        if item_id not in self.item_ids:
            raise ValueError("Item not found")

        if self.inventory[item_id]["quantity"] < quantity:
            raise ValueError("Insufficient stock")

        self.inventory[item_id]["quantity"] -= quantity
        self.sales_counter[item_id] += quantity

    def get_item(self, item_id):
        return self.inventory.get(item_id)

    def get_items_by_category(self, category):
        return [self.inventory[item_id] for item_id in self.categories[category]]

    def low_stock_items(self, threshold=5):
        return [
            item for item in self.inventory.values()
            if item["quantity"] <= threshold
        ]

    def top_selling_items(self, n=5):
        return self.sales_counter.most_common(n)

system = InventorySystem()

system.add_item(1, "Laptop", "Electronics", 10)
system.add_item(2, "Mouse", "Electronics", 50)
system.add_item(3, "Notebook", "Stationery", 100)

system.sell_item(1, 2)
system.sell_item(2, 5)
system.sell_item(1, 1)

print("Item 1:", system.get_item(1))
print("Electronics:", system.get_items_by_category("Electronics"))
print("Low stock:", system.low_stock_items())
print("Top selling:", system.top_selling_items())

system = InventorySystem()

start = time.time()
for i in range(1_000_000):
    system.add_item(i, f"Item{i}", "General", 100)
print("Add time:", time.time() - start)

start = time.time()
for i in range(1_000_000):
    system.get_item(i)
print("Lookup time:", time.time() - start)