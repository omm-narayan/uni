furniture = ['Chair', 'Table', 'Bed', 'Sofa']
cost = [100, 200, 300, 400]

required_furniture = 'Bed'
quantity = 2

bill_amount = 0

if required_furniture in furniture and quantity > 0:
    furniture_index = furniture.index(required_furniture)
    price_per_item = cost[furniture_index]
    bill_amount = price_per_item * quantity
else:
    if required_furniture not in furniture:
        print(f"Error: The furniture '{required_furniture}' is not available.")
    if quantity <= 0:
        print("Error: The quantity to be purchased must be greater than zero.")

print(f"Item: {required_furniture}")
print(f"Quantity: {quantity}")
print(f"Bill Amount: ${bill_amount}")

furniture = ['Chair', 'Table', 'Bed', 'Sofa']
cost = [100, 200, 300, 400]
