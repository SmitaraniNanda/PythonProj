# Products and prices
products = {
    "apple": 2.5,
    "banana": 1.2,
    "milk": 3.0,
    "bread": 2.8
}

# Customer shopping cart (product: quantity)
cart = {
    "apple": 4,
    "milk": 2,
    "bread": 1
}

# Calculate total cost
total = 0
for item in cart:
    price = products[item]
    quantity = cart[item]
    cost = price * quantity
    total += cost
    print(f"{item.title()} * {quantity} = ${cost:.2f}")

print("\nSubtotal:", round(total, 2))

# Apply discount if total is over $20
if total > 20:
    discount = total * 0.1  # 10% discount
    total -= discount
    print("Discount applied: -$", round(discount, 2))

print("Final Total: $", round(total, 2))