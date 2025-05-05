items = [
    {'name': 'Soap', 'price': 25.0, 'quantity': 2},
    {'name': 'Shampoo', 'price': 120.0, 'quantity': 1},
    {'name': 'Toothpaste', 'price': 45.0, 'quantity': 3}
]
total_cost = 0.0
for item in items:
    item_cost = item['price'] * item['quantity']
    total_cost += item_cost
    print(f"{item['name']} - ₹{item['price']} x {item['quantity']} = ₹{item_cost:.2f}")
print(f"\nTotal Bill: ₹{total_cost:.2f}")
