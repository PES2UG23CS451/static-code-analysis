# import json
# import logging
# from datetime import datetime

# # Global variable
# stock_data = {}

# def addItem(item="default", qty=0, logs=[]):
#     if not item:
#         return
#     stock_data[item] = stock_data.get(item, 0) + qty
#     logs.append("%s: Added %d of %s" % (str(datetime.now()), qty, item))

# def removeItem(item, qty):
#     try:
#         stock_data[item] -= qty
#         if stock_data[item] <= 0:
#             del stock_data[item]
#     except:
#         pass

# def getQty(item):
#     return stock_data[item]

# def loadData(file="inventory.json"):
#     f = open(file, "r")
#     global stock_data
#     stock_data = json.loads(f.read())
#     f.close()

# def saveData(file="inventory.json"):
#     f = open(file, "w")
#     f.write(json.dumps(stock_data))
#     f.close()

# def printData():
#     print("Items Report")
#     for i in stock_data:
#         print(i, "->", stock_data[i])

# def checkLowItems(threshold=5):
#     result = []
#     for i in stock_data:
#         if stock_data[i] < threshold:
#             result.append(i)
#     return result

# def main():
#     addItem("apple", 10)
#     addItem("banana", -2)
#     addItem(123, "ten")  # invalid types, no check
#     removeItem("apple", 3)
#     removeItem("orange", 1)
#     print("Apple stock:", getQty("apple"))
#     print("Low items:", checkLowItems())
#     saveData()
#     loadData()
#     printData()
#     eval("print('eval used')")  # dangerous

# main()


"""Inventory management system performing basic stock operations."""

import json
from datetime import datetime

# Global variable
stock_data = {}


def add_item(item="default", qty=0, logs=None):
    """Add an item and quantity to the stock."""
    if logs is None:
        logs = []

    if not item:
        print("Error: Item name cannot be empty.")
        return

    if not isinstance(item, str) or not isinstance(qty, (int, float)):
        print("Invalid item or quantity type.")
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    print(f"Added {qty} of {item} successfully.")


def remove_item(item, qty):
    """Remove a quantity of an item from the stock."""
    if not isinstance(qty, (int, float)) or qty <= 0:
        print("Quantity must be a positive number.")
        return

    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            print(f"Item '{item}' completely removed from stock.")
        else:
            print(f"Removed {qty} of '{item}'. Remaining: {stock_data[item]}")
    except KeyError:
        print(f"Item '{item}' not found in stock.")
    except (TypeError, ValueError) as e:
        print(f"Error removing item: {e}")


def get_qty(item):
    """Return the quantity of a specific item."""
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory data from a JSON file."""
    global stock_data
    try:
        with open(file, "r", encoding="utf-8") as f:
            stock_data = json.load(f)
        print(f"Data loaded successfully from '{file}'.")
    except FileNotFoundError:
        print(f"File '{file}' not found. Starting with empty inventory.")
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{file}'. Starting fresh.")
    except OSError as e:
        print(f"File operation error while loading data: {e}")


def save_data(file="inventory.json"):
    """Save current inventory data to a JSON file."""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=4)
        print(f"Data saved successfully to '{file}'.")
    except OSError as e:
        print(f"Error saving data: {e}")


def print_data():
    """Print all items in the inventory."""
    print("\nItems Report:")
    if not stock_data:
        print("No items in stock.")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def check_low_items(threshold=5):
    """Return a list of items with quantity below the threshold."""
    if not isinstance(threshold, (int, float)) or threshold < 0:
        print("Invalid threshold value.")
        return []

    result = [item for item, qty in stock_data.items() if qty < threshold]
    return result


def main():
    """Main function to demonstrate inventory operations."""
    add_item("apple", 10)
    add_item("banana", -2)
    add_item("grapes", 5)
    remove_item("apple", 3)
    remove_item("orange", 1)
    print(f"Apple stock: {get_qty('apple')}")
    print(f"Low items: {check_low_items()}")
    save_data()
    load_data()
    print_data()


if __name__ == "__main__":
    main()
