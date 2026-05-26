# Expense Tracker 

print("===== Expense Tracker =====")

total = 0

while True:
    print("\n1. Add Expense")
    print("2. View Total Spent")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense = float(input("Enter expense amount: "))

        
        total = total + expense

        print("Expense Added Successfully!")

    elif choice == "2":
        print("Total Spent:", total)

    elif choice == "3":
        print("Thank You for Using Expense Tracker!")
        break

    else:
        print("Invalid Choice! Please enter 1, 2, or 3.")