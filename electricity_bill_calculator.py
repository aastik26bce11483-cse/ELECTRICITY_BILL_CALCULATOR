#ELECTRICITY BILL CALCULATOR
#SLAB RATES PER UNIT
#100 UNITS : Rs 3
#101-200 UNITS : Rs 5
#201-200 UNITS : Rs 7
#ABOVE 300 UNITS : Rs 10
# MINIMUM FIXED CHARGE OF Rs 50 IS ADDED TO EACH BILL.

FIXED_CHARGE = 50
#lists to remember every bill calculated in this session
customer_names = []
units_used = []
bill_amounts = []


def show_menu():
    print("-----ELECTRICITY BILL CALCULATOR-----")
    print("1. Calculate a new bill")
    print("2. View all bills")
    print("3. Exit")


def calculate_energy_charge(units):
    if units <= 100:
        charge = units * 3
    elif units <= 200:
        charge = 100 * 3 + (units - 100) * 5
    elif units <= 300:
        charge = 100 * 3 + 100 * 5 + (units - 200) * 7
    else:
        charge = 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 10
    return charge


def new_bill():
    name = input("ENTER CUSTOMER NAME: ")
    if name == "":
        print("Name cannot be empty")
        return

    units_text = input("Enter units consumed: ")
    if not units_text.isdigit():
        print("Please enter a valid whole number for units.")
        return

    units = int(units_text)
    energy_charge = calculate_energy_charge(units)
    total_charge = energy_charge + FIXED_CHARGE

    print("-----BILL-----")
    print("Customer      : ", name)
    print("Units used    : ", str(units))
    print("Energy charge : Rs. ", str(energy_charge))
    print("Fixed charge  : Rs. ", str(FIXED_CHARGE))
    print("Total charge  : Rs. ", str(total_charge))
    print("------------")

    customer_names.append(name)
    units_used.append(units)
    bill_amounts.append(total_charge)

def view_bills():
    if len(customer_names) == 0:
        print("No bills calculated yet.")
        return
    print("All bills this session:")
    grand_total = 0
    for i in range(len(customer_names)):
        print(str(i+1), ".", customer_names[i], "-", str(units_used[i]), "Units - Rs. ", str(bill_amounts[i]))
        grand_total = grand_total + bill_amounts[i]
        print("Total collected: Rs. ", str(grand_total))


def main():
    while True:
        show_menu()
        choice = input("Enter choice: ")
        if choice == "1":
            new_bill()
        elif choice == "2":
            view_bills()
            print("THANK YOU, GOODBYE!")
        elif choice == "3":
            print("THANK YOU, GOODBYE!")
            break
        else:
            print("Invalid choice. Please enter a valid choice (1,2 or 3).")

main()
