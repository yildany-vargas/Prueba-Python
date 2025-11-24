# # sales_reports.py
# Sales registration and reports for the Inventory & Sales system.

from datetime import date
from collections import Counter
from typing import Dict, Any, List, Tuple, Optional

# Import inventory data and functions
from inventory import inventory, get_product, list_inventory, calculate_inventory_value, is_positive_int

# Sales list: each sale is a dictionary
sales: List[Dict[str, Any]] = []


# -------------------------
# Core functions (with parameters/returns)
# -------------------------
def can_sell(title: str, qty: int) -> Tuple[bool, str]:
    """Check if a product exists and has enough stock."""
    prod = get_product(title)
    if not prod:
        return False, "Product not found."
    if not is_positive_int(qty):
        return False, "Quantity must be a positive integer."
    if qty > prod["quantity"]:
        return False, "Insufficient stock."
    return True, "OK"


def register_sale(client: str, title: str, quantity: int, discount: float = 0.0) -> Tuple[bool, str]:
    """
    Register a sale.
    - client: client's name (letters and spaces)
    - title: product title (must exist)
    - quantity: integer > 0
    - discount: number >= 0 and less than gross
    Returns (True, message) or (False, error)
    """
    try:
        prod = get_product(title)
        if not prod:
            return False, "Product not found."

        if not is_positive_int(quantity):
            return False, "Quantity must be a positive integer."

        if quantity > prod["quantity"]:
            return False, "Insufficient stock."

        gross = prod["price"] * quantity

        if not isinstance(discount, (int, float)):
            return False, "Discount must be a number."

        if discount < 0 or discount >= gross:
            return False, "Discount must be >= 0 and less than gross amount."

        # Update stock
        prod["quantity"] -= quantity

        sale_record = {
            "client": client.strip(),
            "product_title": prod["title"],
            "author": prod["author"],
            "quantity": quantity,
            "date": date.today().isoformat(),
            "price": prod["price"],
            "gross": gross,
            "discount": float(discount),
            "net": gross - float(discount)
        }

        sales.append(sale_record)
        return True, "Sale registered successfully."
    except Exception as e:
        return False, f"Unexpected error while registering sale: {e}"


def list_sales() -> List[Dict[str, Any]]:
    """Return a copy of sales list."""
    return [s.copy() for s in sales]


# -------------------------
# Reports (return data so they can be tested; console wrappers print them)
# -------------------------
def top_n_products(n: int = 3) -> List[Tuple[str, int]]:
    """Return a list of (product_title, total_quantity_sold) ordered descending."""
    counter = Counter()
    for s in sales:
        counter[s["product_title"]] += s["quantity"]
    return counter.most_common(n)


def sales_grouped_by_author() -> Dict[str, float]:
    """Return dict author -> total net income."""
    totals: Dict[str, float] = {}
    for s in sales:
        totals.setdefault(s["author"], 0.0)
        totals[s["author"]] += s["net"]
    return totals


def income_summary() -> Tuple[float, float]:
    """Return (gross_total, net_total)."""
    total_gross = sum(s["gross"] for s in sales)
    total_net = sum(s["net"] for s in sales)
    return total_gross, total_net


# -------------------------
# Console-friendly wrappers
# -------------------------
def prompt_register_sale() -> None:
    """Console flow to register a sale (uses core functions)."""
    print("\n--- Register sale ---")
    try:
        client = input("Client name: ").strip()
        if not client or not client.replace(" ", "").isalpha():
            print("Client name must contain only letters and spaces.")
            return

        # Show available products with stock > 0
        available = [p for p in list_inventory().values() if p["quantity"] > 0]
        if not available:
            print("No products available to sell.")
            return

        for i, p in enumerate(available, start=1):
            print(f"{i}. {p['title']} (stock: {p['quantity']}) - Price: {p['price']:.2f}")

        choice = input("Choose product number: ").strip()
        try:
            idx = int(choice)
            if idx < 1 or idx > len(available):
                print("Invalid product number.")
                return
        except ValueError:
            print("Enter a valid number.")
            return

        selected = available[idx - 1]["title"]

        qty_input = input("Quantity to sell: ").strip()
        try:
            qty = int(qty_input)
        except ValueError:
            print("Enter a valid integer quantity.")
            return

        discount_input = input("Discount in pesos (press Enter if none): ").strip()
        discount = 0.0
        if discount_input != "":
            try:
                discount = float(discount_input)
            except ValueError:
                print("Invalid discount. Using 0.")
                discount = 0.0

        ok, msg = register_sale(client, selected, qty, discount)
        print(msg)
    except Exception as e:
        print(f"Unexpected error in sale flow: {e}")


def prompt_show_reports() -> None:
    """Print the three required reports in a friendly way."""
    print("\n--- Reports ---")
    # Top 3
    print("\nTop 3 best-selling products:")
    top = top_n_products(3)
    if not top:
        print("No sales yet.")
    else:
        for i, (title, qty) in enumerate(top, start=1):
            print(f"{i}. {title} - Sold: {qty}")

    # Sales by author
    print("\nSales grouped by author (net):")
    by_author = sales_grouped_by_author()
    if not by_author:
        print("No sales yet.")
    else:
        for author, total in by_author.items():
            print(f"{author} - Net income: {total:.2f}")

    # Income summary
    gross, net = income_summary()
    print(f"\nTotal gross income: {gross:.2f}")
    print(f"Total net income:   {net:.2f}")