# inventory.py
from typing import Dict, Any, Tuple, Optional

# Constant: initial products (we keep the 5 products you used before)
INITIAL_PRODUCTS = {
    "Cien años de soledad": {
        "title": "Cien años de soledad",
        "author": "Gabriel García Márquez",
        "category": "Novel",
        "price": 45.00,
        "quantity": 10
    },
    "El Principito": {
        "title": "El Principito",
        "author": "Antoine de Saint-Exupéry",
        "category": "Children",
        "price": 30.00,
        "quantity": 8
    },
    "Fundamentos de Python": {
        "title": "Fundamentos de Python",
        "author": "A. Programador",
        "category": "Programming",
        "price": 60.00,
        "quantity": 5
    },
    "La casa de los espíritus": {
        "title": "La casa de los espíritus",
        "author": "Isabel Allende",
        "category": "Novel",
        "price": 50.00,
        "quantity": 6
    },
    "Historia mínima de Colombia": {
        "title": "Historia mínima de Colombia",
        "author": "Varios",
        "category": "History",
        "price": 40.00,
        "quantity": 4
    }
}

# Inventory is a dictionary keyed by title -> product dict
inventory: Dict[str, Dict[str, Any]] = {k: v.copy() for k, v in INITIAL_PRODUCTS.items()}


# -------------------------
# Helper validation functions
# -------------------------
def is_valid_text(value: str) -> bool:
    """Return True if value contains only letters and spaces and is not empty."""
    return bool(value) and value.replace(" ", "").isalpha()


def is_positive_float(value: float) -> bool:
    return isinstance(value, (int, float)) and value > 0


def is_positive_int(value: int) -> bool:
    return isinstance(value, int) and value > 0


# -------------------------
# Core functions (with parameters and returns)
# -------------------------
def add_product(title: str, author: str, category: str, price: float, quantity: int) -> Tuple[bool, str]:
    """
    Add a product to inventory.
    Returns (True, message) if added, (False, error_message) if not.
    """
    try:
        title_key = title.strip()
        if not is_valid_text(title_key):
            return False, "Title must contain only letters and spaces."

        if title_key in inventory:
            return False, "Product already exists."

        if not is_valid_text(author):
            return False, "Author must contain only letters and spaces."

        if not is_valid_text(category):
            return False, "Category must contain only letters and spaces."

        if not is_positive_float(price):
            return False, "Price must be a positive number."

        if not is_positive_int(quantity):
            return False, "Quantity must be a positive integer."

        inventory[title_key] = {
            "title": title_key,
            "author": author.strip(),
            "category": category.strip(),
            "price": float(price),
            "quantity": int(quantity)
        }
        return True, f"Product '{title_key}' added successfully."
    except Exception as e:
        return False, f"Unexpected error while adding product: {e}"


def get_product(title: str) -> Optional[Dict[str, Any]]:
    """Return the product dict or None if not found."""
    return inventory.get(title.strip())


def update_price(title: str, new_price: float) -> Tuple[bool, str]:
    """Update price of product. Returns (success, message)."""
    try:
        prod = get_product(title)
        if not prod:
            return False, "Product not found."
        if not is_positive_float(new_price):
            return False, "New price must be positive."
        prod["price"] = float(new_price)
        return True, "Price updated successfully."
    except Exception as e:
        return False, f"Unexpected error while updating price: {e}"


def update_quantity(title: str, new_quantity: int) -> Tuple[bool, str]:
    """Update quantity of product. Returns (success, message)."""
    try:
        prod = get_product(title)
        if not prod:
            return False, "Product not found."
        if not is_positive_int(new_quantity):
            return False, "New quantity must be a positive integer."
        prod["quantity"] = int(new_quantity)
        return True, "Quantity updated successfully."
    except Exception as e:
        return False, f"Unexpected error while updating quantity: {e}"


def delete_product(title: str) -> Tuple[bool, str]:
    """Delete product by title. Returns (success, message)."""
    try:
        key = title.strip()
        if key in inventory:
            del inventory[key]
            return True, f"Product '{key}' deleted."
        return False, "Product not found."
    except Exception as e:
        return False, f"Unexpected error while deleting product: {e}"


def list_inventory() -> Dict[str, Dict[str, Any]]:
    """Return a copy of the inventory for safe use."""
    return {k: v.copy() for k, v in inventory.items()}


# Use a lambda for aggregated calculation of total inventory value
calculate_inventory_value = lambda inv: sum(p["price"] * p["quantity"] for p in inv.values())


# -------------------------
# Console-friendly wrapper functions (these call core functions)
# -------------------------
def input_text(message: str) -> str:
    while True:
        value = input(message).strip()
        if is_valid_text(value):
            return value
        print("Please enter only letters and spaces (not empty).")


def input_float(message: str) -> float:
    while True:
        val = input(message).strip()
        try:
            num = float(val)
            if is_positive_float(num):
                return num
            print("Enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid decimal number (e.g., 12.50).")


def input_int(message: str) -> int:
    while True:
        val = input(message).strip()
        try:
            num = int(val)
            if is_positive_int(num):
                return num
            print("Enter an integer greater than 0.")
        except ValueError:
            print("Please enter a valid integer (e.g., 3).")