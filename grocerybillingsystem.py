# Grocery Store Billing System
# Case Study 1

# Initialize total amount
total = 0

print("------ Grocery Store Billing System ------")

# Loop to accept price and quantity for 5 items
for i in range(1, 6):
    print(f"\nItem {i}")
    
    price = float(input("Enter price of item: Rs. "))
    quantity = int(input("Enter quantity: "))
    
    item_total = price * quantity
    total += item_total

# Display original total
print("\n------------------------------------------")
print(f"Original Total Amount: Rs. {total:.2f}")

# Apply discount if total > 100
discount = 0
if total > 100:
    discount = total * 0.10
    print(f"Discount Applied (10%): Rs. {discount:.2f}")
else:
    print("No Discount Applied")

# Calculate final payable amount
final_amount = total - discount

print(f"Final Payable Amount: Rs. {final_amount:.2f}")
print("------------------------------------------")
