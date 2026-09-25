storage = [
    {"name": "apple", "price": 1.2, "quantity": 10},
    {"name": "banana", "price": 0.8, "quantity": 15},
    {"name": "orange", "price": 1.5, "quantity": 2},
    {"name": "kiwi", "price": 2.0, "quantity": 3},
    {"name": "grape", "price": 2.5, "quantity": 8}
] #tao kho

storage_sorted = sorted(storage, key=lambda storage: storage["quantity"], reverse=True) #sap xep kho theo so luong giam dan


print("|","-" * 46, "|")
print(f"|{'item':<11} | {'quantity':<10} | {'price':<10}| {'value':<9}|")
print("|","-" * 46, "|")
total_value = 0
total_quantity = 0
for item in storage_sorted:
    item_value = item["price"] * item["quantity"]
    total_value += item_value
    total_quantity += item["quantity"]

    print(f"|-{item['name']:<10} | {item['quantity']:<10} | {item['price']:<10.2f}| {item_value:<9.2f}|")
print("|","-" * 46, "|")
print(f"|{'Total':<11} | {total_quantity:<10} | {' ':<9} | {total_value:<9.2f}|")
print("|","-" * 46, "|")
print(f"Warning: Low stock items (quantity < 5):")  
for item in storage:
    if item["quantity"] < 5:
        print(f"-{item['name']} (Quantity: {item['quantity']})")   