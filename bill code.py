"""
Mini Project: Supermarket Bill Generation
Author: Tejesh
"""

from datetime import datetime

# Input customer name
name = input("Enter your name: ")

# List of items in the store (display purpose)
lists = '''
sugar   Rs 30/kg
rice    Rs 110/kg
salt    Rs 32/kg
oil     Rs 170/liter
paneer  Rs 110/kg
colgate Rs 76/each
maggi   Rs 50/kg
boost   Rs 32/each
'''

# Items and prices (dictionary format)
items = {
    "sugar": 30,
    "rice": 110,
    "salt": 32,
    "oil": 170,
    "paneer": 110,
    "colgate": 76,
    "maggi": 50,
    "boost": 32
}

# Initialize variables
pricelist = []
totalprice = 0
ilist = []
qlist = []
plist = []

# Show item list
option = int(input("Enter 1 to show the supermarket item list: "))
if option == 1:
    print(lists)

# Loop to add items to cart
for i in range(len(items)):
    inp1 = int(input("Press 1 to buy an item or 2 to exit: "))
    if inp1 == 2:
        break
    elif inp1 == 1:
        item = input("Enter the item name: ").lower()
        quantity = int(input("Enter the quantity: "))
        if item in items:
            price = quantity * items[item]
            pricelist.append((item, quantity, items[item], price))
            totalprice += price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
        else:
            print("Sorry, the item you entered is not available.")
    else:
        print("Invalid input! Please press 1 or 2.")

# Billing section
inp = input("Can I bill the items? (yes/no): ").lower()
if inp == "yes":
    if totalprice != 0:
        gst = (totalprice * 5) / 100
        finalamount = gst + totalprice

        print("=" * 25, "TEJA SUPERMARKET", "=" * 25)
        print(" " * 28, "Rajahmundry")
        print("Name:", name, " " * (40 - len(name)), "Date:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print("-" * 75)
        print("S.No", " " * 5, "Item", " " * 10, "Quantity", " " * 5, "Price")
        for i in range(len(pricelist)):
            print(i + 1, " " * 8, ilist[i], " " * (15 - len(ilist[i])), qlist[i], " " * 10, plist[i])
        print("-" * 75)
        print(" " * 50, 'Total Amount: Rs', totalprice)
        print(" " * 50, 'GST (5%): Rs', round(gst, 2))
        print("-" * 75)
        print(" " * 50, 'Final Amount: Rs', round(finalamount, 2))
        print("-" * 75)
        print(" " * 50, "Thanks for visiting!")
        print("-" * 75)
    else:
        print("No items were purchased.")
else:
    print("Thank you. Visit again.")
