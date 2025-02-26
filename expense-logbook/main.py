"""
Collin Maassen Personal Project
Inventory management and expense tracking for side businesses.
As well as income tracking
"""
import expense
import product
import inventory
import business
import report


print("Hello, welcome to your personal Inventory/Expense tracker ")

def main():
    while True:
        print("\nWhat action would you like to take? \n")
        print("1. Enter data for a current business.")
        print("2. Add or edit business information.")
        print("3. Save and Exit.")

        try:
            choice = int(input("\nEnter Desired Action: "))
            if choice == 1:
                print("Select the business id from the list below: ")

            elif choice == 2:
            elif choice == 3:
        except ValueError:
            print("Invalid input. Please enter a number.")

        #     elif choice == 4:
        #     elif choice == 5:
        #     elif choice == 6:
            
        # print("\nWhat action would you like to perform?")
        # print("1. Enter New Expense/Income")
        # print("2. Enter New or Update Product Information")
        # print("3. Inventory Check/ Report")
        # print("4. Enter New Business Information")
        # print("5. Pull Expense/Income Report")
        # print("6. Save Progress")

        