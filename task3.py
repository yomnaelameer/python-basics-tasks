correct_pin = 1234
balance = 5000

pin = int(input("Enter your PIN: "))

if pin == correct_pin:

    print("1 - Withdraw")
    print("2 - Check Balance")

    choice = int(input("Choose an option: "))

    if choice == 2:
        print("Your current balance is:", balance)

    elif choice == 1:
        amount = float(input("Enter withdrawal amount: "))

        if amount > balance:
            print("Sorry, insufficient balance.")
        else:
            balance = balance - amount
            print("Transaction successful.")
            print("Remaining balance:", balance)

    else:
        print("Invalid choice.")

else:
    print("Incorrect PIN. Transaction rejected.")