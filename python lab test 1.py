balance = 0
transactions = []

while True:
    print("\n===== BANKING TRANSACTION SIMULATOR =====")
    print("1. Deposit")
    print("2. Withdrawal")
    print("3. Balance Inquiry")
    print("4. Transaction History")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        amount = float(input("Enter deposit amount: "))

        if amount <= 0:
            print("Invalid amount! Enter a positive amount.")
        else:
            balance += amount
            transactions.append(("Deposit", amount, balance))
            print("Amount deposited successfully!")
            print("Current Balance:", balance)

    elif choice == '2':
        amount = float(input("Enter withdrawal amount: "))

        if amount <= 0:
            print("Invalid amount! Enter a positive amount.")
        elif amount > balance:
            print("Insufficient balance!")
        else:
            balance -= amount
            transactions.append(("Withdrawal", amount, balance))
            print("Withdrawal successful!")
            print("Current Balance:", balance)

    elif choice == '3':
        print("Current Balance:", balance)

    elif choice == '4':
        print("\n===== TRANSACTION HISTORY =====")

        if not transactions:
            print("No transactions found.")
        else:
            for transaction in transactions:
                print("Type:", transaction[0],
                      "| Amount:", transaction[1],
                      "| Balance:", transaction[2])

    elif choice == '5':
        print("Thank you for using our banking simulator!")
        break

    else:
        print("Invalid choice! Please select between 1 and 5.")