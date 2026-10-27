#Algorithm
Start the program.
Initialize product details, prices, and available stock.
Accept customer orders containing product IDs and quantities.
Validate orders against available stock.
Calculate order totals and apply discounts.
Process dispatches and update inventory.
Process customer returns and restore returned quantities to stock.
Calculate net revenue after discounts and refunds.
Compare expected stock with recorded stock to identify discrepancies.
Display the order report, revenue summary, discrepancies, and final inventory.
Stop the program.
#flowchart
       +---------------------------+
       |           START           |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Initialize Product Stock  |
       | and Price Details         |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Enter Customer Orders     |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Validate Orders and Stock |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Calculate Totals and      |
       | Apply Discounts           |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Process Dispatches        |
       | and Update Stock          |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Process Returns and       |
       | Calculate Refunds         |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Reconcile Stock and       |
       | Calculate Revenue         |
       +---------------------------+
                    |
                    v
       +---------------------------+
       | Display Final Reports     |
       +---------------------------+
                    |
                    v
       +---------------------------+
       |            END            |
       +---------------------------+
#code
# Integrated E-Commerce Order Processing and Reconciliation

products = {
    101: {"name": "Laptop", "price": 50000, "stock": 10},
    102: {"name": "Headphones", "price": 2000, "stock": 20},
    103: {"name": "Keyboard", "price": 1500, "stock": 15}
}

initial_stock = {
    product_id: details["stock"]
    for product_id, details in products.items()
}

orders = {}
total_revenue = 0
total_refunds = 0


def display_products():
    print("\nAVAILABLE PRODUCTS")
    print("-" * 55)
    print(f"{'ID':<10}{'Product':<15}{'Price':<15}{'Stock':<10}")

    for product_id, details in products.items():
        print(f"{product_id:<10}{details['name']:<15}"
              f"Rs.{details['price']:<12}{details['stock']:<10}")


def process_order():
    global total_revenue

    order_id = input("\nEnter order ID: ").strip()

    if not order_id:
        print("Order ID cannot be empty.")
        return

    if order_id in orders:
        print("Duplicate order ID!")
        return

    try:
        product_id = int(input("Enter product ID: "))
        quantity = int(input("Enter quantity: "))

        if product_id not in products:
            print("Invalid product ID.")
            return

        if quantity <= 0:
            print("Quantity must be positive.")
            return

        product = products[product_id]

        if quantity > product["stock"]:
            print("Insufficient stock. Order rejected.")
            return

        subtotal = product["price"] * quantity

        # Discount rules
        if subtotal >= 20000:
            discount_rate = 0.10
        elif subtotal >= 5000:
            discount_rate = 0.05
        else:
            discount_rate = 0.0

        discount = subtotal * discount_rate
        final_amount = subtotal - discount

        # Dispatch the complete order
        product["stock"] -= quantity

        orders[order_id] = {
            "product_id": product_id,
            "quantity": quantity,
            "dispatched": quantity,
            "returned": 0,
            "subtotal": subtotal,
            "discount": discount,
            "revenue": final_amount
        }

        total_revenue += final_amount

        print("\nORDER PROCESSED SUCCESSFULLY")
        print("Order ID:", order_id)
        print("Product:", product["name"])
        print("Subtotal: Rs.", round(subtotal, 2))
        print("Discount: Rs.", round(discount, 2))
        print("Final Amount: Rs.", round(final_amount, 2))
        print("Dispatch Status: Dispatched")

    except ValueError:
        print("Invalid input! Enter numeric product IDs and quantities.")


def process_return():
    global total_revenue, total_refunds

    order_id = input("\nEnter order ID for return: ").strip()

    if order_id not in orders:
        print("Order not found.")
        return

    order = orders[order_id]
    returnable = order["dispatched"] - order["returned"]

    if returnable <= 0:
        print("No items are available for return.")
        return

    try:
        quantity = int(input("Enter return quantity: "))

        if quantity <= 0 or quantity > returnable:
            print("Invalid return quantity.")
            return

        product = products[order["product_id"]]

        # Refund based on the discounted price
        unit_refund = (
            order["subtotal"] - order["discount"]
        ) / order["quantity"]

        refund = unit_refund * quantity

        order["returned"] += quantity
        product["stock"] += quantity

        order["revenue"] -= refund
        total_revenue -= refund
        total_refunds += refund

        print("\nRETURN PROCESSED SUCCESSFULLY")
        print("Product:", product["name"])
        print("Returned Quantity:", quantity)
        print("Refund: Rs.", round(refund, 2))
        print("Stock Updated:", product["stock"])

    except ValueError:
        print("Invalid input! Enter an integer quantity.")


def reconcile_inventory():
    print("\nINVENTORY RECONCILIATION")
    print("-" * 75)
    print(f"{'Product':<15}{'Initial':<10}{'Sold':<10}"
          f"{'Returned':<12}{'Expected':<12}{'Recorded':<10}")
    print("-" * 75)

    discrepancies = 0

    for product_id, product in products.items():
        sold = sum(
            order["dispatched"]
            for order in orders.values()
            if order["product_id"] == product_id
        )

        returned = sum(
            order["returned"]
            for order in orders.values()
            if order["product_id"] == product_id
        )

        expected_stock = initial_stock[product_id] - sold + returned
        recorded_stock = product["stock"]

        print(f"{product['name']:<15}"
              f"{initial_stock[product_id]:<10}"
              f"{sold:<10}"
              f"{returned:<12}"
              f"{expected_stock:<12}"
              f"{recorded_stock:<10}")

        if expected_stock != recorded_stock:
            discrepancies += 1
            print("  DISCREPANCY DETECTED!")

    print("-" * 75)

    if discrepancies == 0:
        print("Inventory Status: Reconciled successfully.")
    else:
        print("Inventory Status: Discrepancies detected:", discrepancies)


def final_summary():
    print("\n========== FINAL E-COMMERCE SUMMARY ==========")

    print("\nProduct Inventory:")
    for product_id, product in products.items():
        print(f"{product['name']}: {product['stock']} copies/items")

    print("\nOrder Details:")
    print("Total Orders:", len(orders))

    total_discount = sum(
        order["discount"] for order in orders.values()
    )

    gross_sales = sum(
        order["subtotal"] for order in orders.values()
    )

    print("Gross Sales: Rs.", round(gross_sales, 2))
    print("Total Discounts: Rs.", round(total_discount, 2))
    print("Total Refunds: Rs.", round(total_refunds, 2))
    print("Net Revenue: Rs.", round(total_revenue, 2))

    reconcile_inventory()


def main():
    while True:
        print("\n===== E-COMMERCE ORDER MANAGEMENT =====")
        print("1. Display Products")
        print("2. Process Order")
        print("3. Process Return")
        print("4. Reconcile Inventory")
        print("5. Final Summary")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            display_products()
        elif choice == "2":
            process_order()
        elif choice == "3":
            process_return()
        elif choice == "4":
            reconcile_inventory()
        elif choice == "5":
            final_summary()
        elif choice == "6":
            print("Thank you for using the system!")
            break
        else:
            print("Invalid choice! Please select 1 to 6.")


if __name__ == "__main__":
    main()
    #sample output
    ===== E-COMMERCE ORDER MANAGEMENT =====
1. Display Products
2. Process Order
3. Process Return
4. Reconcile Inventory
5. Final Summary
6. Exit

Enter your choice: 2

Enter order ID: ORD101
Enter product ID: 102
Enter quantity: 3

ORDER PROCESSED SUCCESSFULLY
Order ID: ORD101
Product: Headphones
Subtotal: Rs. 6000
Discount: Rs. 300.0
Final Amount: Rs. 5700.0
Dispatch Status: Dispatched
Enter your choice: 3

Enter order ID for return: ORD101
Enter return quantity: 1

RETURN PROCESSED SUCCESSFULLY
Product: Headphones
Returned Quantity: 1
Refund: Rs. 1900.0
Stock Updated: 18
Enter your choice: 5

========== FINAL E-COMMERCE SUMMARY ==========

Product Inventory:
Laptop: 10 copies/items
Headphones: 18 copies/items
Keyboard: 15 copies/items

Order Details:
Total Orders: 1
Gross Sales: Rs. 6000
Total Discounts: Rs. 300.0
Total Refunds: Rs. 1900.0
Net Revenue: Rs. 3800.0

INVENTORY RECONCILIATION
---------------------------------------------------------------------------
Product        Initial   Sold      Returned    Expected    Recorded
---------------------------------------------------------------------------
Laptop         10        0         0           10          10
Headphones     20        3         1           18          18
Keyboard       15        0         0           15          15
---------------------------------------------------------------------------
Inventory Status: Reconciled successfully.