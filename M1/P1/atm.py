stored_pin = '1234'
balance = 1000
attempts_remaining = 3
is_authenticated = False

while attempts_remaining > 0 and not is_authenticated:
    entered_pin = input("Enter PIN: ")
    if entered_pin == stored_pin:
        is_authenticated = True
        print("Access granted.")
    else:
        attempts_remaining -= 1
        print("Incorrect PIN.")
        print("Attempts left:", attempts_remaining)
if not is_authenticated:
    print("Account locked.")
else:
    while True:
        print("\n1. Check Balance")
        print("2. Withdraw")
        print("3. Deposit")
        print("4. Exit")
        choice = input("Choose option: ")
        if choice == "1":
            print("Balance:", balance)
        elif choice == "2":
            amount = float(input("Enter withdrawal amount: "))
            if amount <= 0:
                print("Invalid amount.")
            elif amount > balance:
                print("Insufficient funds.")
            else:
                balance -= amount
                print("Withdrawal successful.")
        elif choice == "3":
            amount = float(input("Enter deposit amount: "))
            if amount <= 0:
                print("Invalid amount.")
            else:
                balance += amount
                print("Deposit auccessful.")
        elif choice == "4":
            print("Session ended.")
            break
        else:
            print("Invalid choice.")
            