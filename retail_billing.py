#Algorithm

Step 1: Start the program.

Step 2: Read the number of products to be purchased.

Step 3: For each product, input:

Product name
Category
Quantity
Unit price

Step 4: Calculate the subtotal for each product.

$$ \text{Subtotal} = \text{Quantity} \times \text{Unit Price} $$

Step 5: Calculate category-specific tax:

Electronics: 18%
Clothing: 5%
Groceries: 0%
Step 6: Calculate the total subtotal of all products.

Step 7: Apply threshold-based discounts:

Subtotal ≥ ₹5,000: 10% discount
Subtotal ≥ ₹2,000: 5% discount
Otherwise: No discount

Step 8: Apply the maximum concession limit of ₹1,000.

Step 9: Calculate the final bill by subtracting the discount from the subtotal and adding the applicable taxes.

Step 10: Display the itemized invoice with product details, taxes, discount, and final amount.

Step 11: Stop the program.
#FLOWCHAT
          ┌───────────────┐
          │     START     │
          └───────┬───────┘
                  │
          ┌───────▼───────┐
          │ Input Number  │
          │  of Products  │
          └───────┬───────┘
                  │
          ┌───────▼───────┐
          │ Enter Product │
          │ Details       │
          └───────┬───────┘
                  │
          ┌───────▼───────┐
          │ Calculate     │
          │ Item Subtotal │
          └───────┬───────┘
                  │
          ┌───────▼───────┐
          │ Calculate     │
          │ Category Tax  │
          └───────┬───────┘
                  │
          ┌───────▼───────┐
          │ More Products?│
          └───────┬───────┘
                  │
             Yes  │  No
             ┌────┘  └─────────────┐
             │                     │
      ┌──────▼───────┐      ┌──────▼────────┐
      │ Enter Next   │      │ Calculate     │
      │ Product      │      │ Total Subtotal│
      └──────┬───────┘      └──────┬────────┘
             │                     │
             └── Repeat     ┌──────▼────────┐
                            │ Apply Discount│
                            │ and Limit      │
                            └──────┬────────┘
                                   │
                            ┌──────▼────────┐
                            │ Calculate Final│
                            │ Bill           │
                            └──────┬────────┘
                                   │
                            ┌──────▼────────┐
                            │ Print Invoice │
                            └──────┬────────┘
                                   │
                            ┌──────▼────────┐
                            │     STOP      │
                            └───────────────┘
#PYTHON CODE
# Retail Billing with Multiple Discount Rules

MAX_DISCOUNT = 1000

products = []
total_subtotal = 0
total_tax = 0

# Input number of products
n = int(input("Enter number of products: "))

# Process each product
for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/groceries): ").lower()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter unit price: "))

    # Calculate subtotal
    subtotal = quantity * price

    # Category-specific tax
    if category == "electronics":
        tax_rate = 18
    elif category == "clothing":
        tax_rate = 5
    elif category == "groceries":
        tax_rate = 0
    else:
        print("Invalid category. Tax set to 0%.")
        tax_rate = 0

    tax = subtotal * tax_rate / 100

    # Store product details
    products.append({
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "subtotal": subtotal,
        "tax": tax,
        "tax_rate": tax_rate
    })

    total_subtotal += subtotal
    total_tax += tax

# Apply threshold-based discount
if total_subtotal >= 5000:
    discount = total_subtotal * 0.10
elif total_subtotal >= 2000:
    discount = total_subtotal * 0.05
else:
    discount = 0

# Apply maximum concession limit
discount = min(discount, MAX_DISCOUNT)

# Calculate final bill
final_bill = total_subtotal - discount + total_tax

# Print invoice
print("\n" + "=" * 65)
print("                 RETAIL BILLING INVOICE")
print("=" * 65)

print(f"{'Product':<15}{'Qty':<6}{'Price':<10}"
      f"{'Subtotal':<12}{'Tax':<10}")

print("-" * 65)

for p in products:
    print(f"{p['name']:<15}{p['quantity']:<6}"
          f"{p['price']:<10.2f}{p['subtotal']:<12.2f}"
          f"{p['tax']:<10.2f}")

print("-" * 65)
print(f"Total Subtotal : Rs. {total_subtotal:.2f}")
print(f"Total Tax      : Rs. {total_tax:.2f}")
print(f"Discount       : Rs. {discount:.2f}")
print(f"Final Bill     : Rs. {final_bill:.2f}")
print("=" * 65)
print("Thank you for shopping!")
#SAMPLE OUTPUT
Enter number of products: 3

Product 1
Enter product name: Laptop
Enter category (electronics/clothing/groceries): electronics
Enter quantity: 1
Enter unit price: 40000

Product 2
Enter product name: Shirt
Enter category (electronics/clothing/groceries): clothing
Enter quantity: 2
Enter unit price: 800

Product 3
Enter product name: Rice
Enter category (electronics/clothing/groceries): groceries
Enter quantity: 2
Enter unit price: 100

=================================================================
                 RETAIL BILLING INVOICE
=================================================================
Product        Qty   Price     Subtotal    Tax
-----------------------------------------------------------------
Laptop         1     40000.00  40000.00    7200.00
Shirt          2     800.00    1600.00     80.00
Rice           2     100.00    200.00      0.00
-----------------------------------------------------------------
Total Subtotal : Rs. 41800.00
Total Tax      : Rs. 7280.00
Discount       : Rs. 1000.00
Final Bill     : Rs. 48080.00
=================================================================
Thank you for shopping!