print("Welcome to the Instant Discount System")

amount = float(input("Enter the purchase amount: "))

if amount < 100:
    discount = 0
elif amount < 500:
    discount = amount * 0.10
else:
    discount = amount * 0.20

final_amount = amount - discount

print("Your available discount is:", discount)
print("The final amount after discount is:", final_amount)