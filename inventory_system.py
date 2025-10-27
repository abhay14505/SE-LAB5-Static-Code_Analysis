"""Inventory Management System - Final Version"""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add specified quantity of an item to inventory."""
    if logs is None:
        logs = []
    if not isinstance(item, str) or not isinstance(qty, int):
        print("Invalid input types for add_item().")
        return
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")


def remove_item(item, qty):
    """Remove specified quantity of an item from inventory."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        print(f"Item '{item}' not found in stock.")


def get_qty(item):
    """Return current quantity of the given item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from JSON file and return it."""
    try:
        with open(file, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
        return {}


def save_data(file="inventory.json"):
    """Save inventory data to JSON file."""
    with open(file, "w", encoding="utf-8") as f:
        json.dump(stock_data, f, indent=4)


def print_data():
    """Print inventory report."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items below the given quantity threshold."""
    return [item for item, qty in stock_data.items() if qty < threshold]


def main():
    """Main program entry point for inventory management."""
    add_item("apple", 10)
    add_item("banana", 2)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print("Low items:", check_low_items())
    save_data()
    loaded_data = load_data()
    stock_data.clear()
    stock_data.update(loaded_data)
    print_data()


if __name__ == "__main__":
    main()
