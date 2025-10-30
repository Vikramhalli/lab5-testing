import json
import logging
from datetime import datetime

# Setup logging configuration
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Global variable for stock
stock_data = {}

def add_item(item="default", qty=0, logs=None):
    """Add a quantity of an item to the stock.

    Args:
        item (str): Item name to add.
        qty (int): Quantity to add.
        logs (list, optional): Log list to record actions.
    """
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.error("Invalid item or quantity type.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def remove_item(item, qty):
    """Remove quantity of an item from stock.

    Args:
        item (str): Item name to remove.
        qty (int): Quantity to remove.
    """
    try:
        if item not in stock_data:
            raise KeyError(f"Item '{item}' not found")
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError as e:
        logging.warning(e)

def get_qty(item):
    """Get current quantity of an item.

    Args:
        item (str): Item name to query.

    Returns:
        int: Quantity available, 0 if not found.
    """
    return stock_data.get(item, 0)

def load_data(file="inventory.json"):
    """Load stock data from JSON file.

    Args:
        file (str): Path to file to load from.
    """
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning("Inventory file not found, starting with empty data.")

def save_data(file="inventory.json"):
    """Save stock data to JSON file.

    Args:
        file (str): Path to file to save to.
    """
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)

def print_data():
    """Print item stock report to console."""
    print("Items Report:")
    for i, qty in stock_data.items():
        print(f"{i} -> {qty}")

def check_low_items(threshold=5):
    """Return list of items with quantity below threshold.

    Args:
        threshold (int): Threshold below which items are considered low.

    Returns:
        list: List of item names with low stock.
    """
    return [i for i, qty in stock_data.items() if qty < threshold]

def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types handled
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
