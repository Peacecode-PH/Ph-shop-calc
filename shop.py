# My PH Shop Calculator
shirt_price = int(input("How much is one shirt? N"))
quantity = int(input("How many did customer buy? "))

total = shirt_price * quantity
print("--- RECEIPT ---")
print("Total to collect is: N", total)

paid = int(input("How much did customer pay? N"))
change = paid - total

print("Your change is: N", change)
print("Thank you! Come again")
