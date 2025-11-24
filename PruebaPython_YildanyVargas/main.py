# main.py
# Main menu for the Inventory & Sales system.

from inventory import (
    list_inventory, input_text, input_float, input_int,
    add_product, get_product, update_price, update_quantity, delete_product, calculate_inventory_value
)
from sales_reports import (
    prompt_register_sale, list_sales, prompt_show_reports, register_sale, list_sales as get_sales
)

# Console menu (simple and beginner-friendly)
def show_menu() -> None:
    print("\n=== Inventory & Sales System ===")
    print("1. Add product")
    print("2. Search product")
    print("3. Update price")
    print("4. Update quantity")
    print("5. Delete product")
    print("6. View inventory")
    print("7. Total inventory value")
    print("8. Register sale")
    print("9. View sales")
    print("10. Reports (Top 3, by author, income)")
    print("11. Quit")


def action_add_product() -> None:
    print("\n--- Add product ---")
    title = input_text("Title: ")
    author = input_text("Author: ")
    category = input_text("Category: ")
    price = input_float("Price: ")
    qty = input_int("Quantity in stock: ")

    success, message = add_product(title, author, category, price, qty)
    print(message)


def action_search_product() -> None:
    print("\n--- Search product ---")
    title = input_text("Product title: ")
    prod = get_product(title)
    if prod:
        print(f"Title: {prod['title']}")
        print(f"Author: {prod['author']}")
        print(f"Category: {prod['category']}")
        print(f"Price: {prod['price']:.2f}")
        print(f"Quantity: {prod['quantity']}")
    else:
        print("Product not found.")


def action_update_price() -> None:
    print("\n--- Update price ---")
    title = input_text("Product title: ")
    new_price = input_float("New price: ")
    ok, msg = update_price(title, new_price)
    print(msg)


def action_update_quantity() -> None:
    print("\n--- Update quantity ---")
    title = input_text("Product title: ")
    new_qty = input_int("New quantity: ")
    ok, msg = update_quantity(title, new_qty)
    print(msg)


def action_delete_product() -> None:
    print("\n--- Delete product ---")
    title = input_text("Product title: ")
    ok, msg = delete_product(title)
    print(msg)


def action_view_inventory() -> None:
    print("\n--- Inventory ---")
    inv = list_inventory()
    if not inv:
        print("Inventory is empty.")
        return
    for t, p in inv.items():
        print(f"{t} — Author: {p['author']} — Category: {p['category']} — Price: {p['price']:.2f} — Qty: {p['quantity']}")


def action_total_value() -> None:
    inv = list_inventory()
    total = calculate_inventory_value(inv)
    print(f"\nTotal inventory value: {total:.2f}")


def action_view_sales() -> None:
    print("\n--- Registered sales ---")
    s = get_sales()
    if not s():
        print("No sales registered yet.")
        return
    for sale in s():
        print(f"{sale['date']} - {sale['client']} bought {sale['quantity']} of {sale['product_title']} (Net: {sale['net']:.2f})")


def main() -> None:
    print("Welcome! This system follows the performance test requirements.")
    while True:
        try:
            show_menu()
            choice = input("Choose an option (1-11): ").strip()
            if choice == "1":
                action_add_product()
            elif choice == "2":
                action_search_product()
            elif choice == "3":
                action_update_price()
            elif choice == "4":
                action_update_quantity()
            elif choice == "5":
                action_delete_product()
            elif choice == "6":
                action_view_inventory()
            elif choice == "7":
                action_total_value()
            elif choice == "8":
                prompt_register_sale()
            elif choice == "9":
                action_view_sales()
            elif choice == "10":
                prompt_show_reports()
            elif choice == "11":
                print("Thank you. Goodbye!")
                break
            else:
                print("Please select a valid option (1-11).")
        except Exception as e:
            # General exception handler to avoid abrupt program stop
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()