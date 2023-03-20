total_price = 0
item_number = int(input("Number of items: "))
while item_number < 0:
    print("Invalid number of items!")
    item_number = int(input("Number of items: "))
for i in range(item_number):
    item_price = float(input("Price of item: "))
    total_price += item_price
if total_price > 100:
    total_price *= 0.9
print(f"Total price for {item_number} items is ${total_price:.2f}")