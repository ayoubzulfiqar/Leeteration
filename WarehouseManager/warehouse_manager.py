class WarehouseManager:
    def __init__(self):
        self.stock = {}

    def add_item(self, item_name, quantity):
        """
        Adds a specified quantity of an item to the warehouse.
        If the item already exists, its quantity is increased.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            print(f"Error: Quantity must be a positive integer. Got {quantity} for {item_name}.")
            return False
        
        self.stock[item_name] = self.stock.get(item_name, 0) + quantity
        print(f"Added {quantity} of {item_name}. New stock: {self.stock[item_name]}")
        return True

    def remove_item(self, item_name, quantity):
        """
        Removes a specified quantity of an item from the warehouse.
        If the item does not exist or insufficient stock, a warning is issued.
        """
        if not isinstance(quantity, int) or quantity <= 0:
            print(f"Error: Quantity to remove must be a positive integer. Got {quantity} for {item_name}.")
            return False

        if item_name not in self.stock:
            print(f"Error: {item_name} not found in warehouse.")
            return False
        
        current_stock = self.stock[item_name]
        if current_stock < quantity:
            print(f"Warning: Not enough {item_name} in stock. Removing {current_stock} instead of {quantity}.")
            self.stock[item_name] = 0
            if current_stock == 0:
                del self.stock[item_name] # Remove item if stock becomes 0
            return False # Indicate partial or failed removal
        else:
            self.stock[item_name] -= quantity
            if self.stock[item_name] == 0:
                del self.stock[item_name] # Remove item if stock becomes 0
            print(f"Removed {quantity} of {item_name}. New stock: {self.stock.get(item_name, 0)}")
            return True

    def get_stock(self, item_name):
        """
        Returns the current quantity of a specific item.
        Returns 0 if the item is not in stock.
        """
        return self.stock.get(item_name, 0)

    def list_all_items(self):
        """
        Prints and returns a dictionary of all items currently in the warehouse
        along with their quantities.
        """
        if not self.stock:
            print("Warehouse is empty.")
            return {}
        
        print("Current Warehouse Stock:")
        for item, quantity in self.stock.items():
            print(f"- {item}: {quantity}")
        return self.stock.copy()

if __name__ == "__main__":
    manager = WarehouseManager()

    print("--- Initializing Warehouse ---")
    manager.list_all_items()

    print("\n--- Adding Items ---")
    manager.add_item("Laptop", 10)
    manager.add_item("Mouse", 50)
    manager.add_item("Keyboard", 25)
    manager.add_item("Laptop", 5) # Add more laptops
    manager.add_item("Monitor", 0) # Invalid add attempt
    manager.add_item("Webcam", -2) # Invalid add attempt

    print("\n--- Checking Stock ---")
    print(f"Stock of Laptop: {manager.get_stock('Laptop')}")
    print(f"Stock of Mouse: {manager.get_stock('Mouse')}")
    print(f"Stock of Headphones: {manager.get_stock('Headphones')}") # Non-existent item

    print("\n--- Listing All Items ---")
    manager.list_all_items()

    print("\n--- Removing Items ---")
    manager.remove_item("Mouse", 20)
    manager.remove_item("Keyboard", 30) # Try to remove more than available
    manager.remove_item("Monitor", 5) # Remove non-existent item
    manager.remove_item("Laptop", 15) # Remove all laptops
    manager.remove_item("Laptop", 1) # Try to remove from empty stock
    manager.remove_item("Mouse", 0) # Invalid remove attempt

    print("\n--- Final Stock ---")
    manager.list_all_items()

    print("\n--- Demonstrating empty warehouse after further removals ---")
    manager.remove_item("Mouse", 30) # Remove remaining mice
    manager.list_all_items()