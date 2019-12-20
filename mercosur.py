"""
Program: WareHouse inventory contorl system
Functionality:
        -Register new items
        id(auto generated)
        title
        catehory
        price
        stock
    -Print all the items
    -Update the stock of a selected item
    -Print items with no stock
    -Remove items

    -Print Different Categories
    -Print Stock Value (sum(price * stock))

    -Register purchase
    -Register sell

    -Log of events
        time | action | itemId
        12:20 | sell | 98
        
        1 - generate log string inside important functions
        2 - add that string to logs array
        3 - save logs array
        4 - load logs array when system starts

"""
from menu import print_menu
from item import Item
import datetime
import pickle
import os
from csv import reader



logs = []
items = []
id_count = 1
items_file = "item.data"
logs_file = "logs.data"

def clear():
    return os.system("cls")

def get_time():
    current_date = datetime.datetime.now()
    time = current_date.strftime("%x")
    return time

def save_items():
    # open creates/ opens a file
    # wb = writes binary info
    writer = open(items_file, "wb")
    #converts the object inot binary and writes it on the file
    pickle.dump(items, writer)
    writer.close() # close the file stream (to release the file)
    print(" Data Has Been Saved")

def save_log():
    # open creates/ opens a file
    # wb = write binary info
    writer = open(logs_file, "wb")
    # converts the object into binary and writes it on the file
    pickle.dump(logs, writer)
    writer.close() # close the file stream (to release the file)
    print(" Log Saved on Secret-Server")

def read_items():
    global id_count # import variables into fn scope

    try:
        reader = open(items_file, "rb") # rb = open the file to the Read Binary
        # read the binary and convert it to the original object
        temp_list = pickle.lead(reader)

        for item in temp_list:
            items.append(item)

            last = items[-1]
            id_couunt = last.id + 1
            print(" Loaded " + str(len(temp_list)) + " items")
    except:
        # you get here if you try block crashes
        print(" *Error: Datas could not be loaded!")

def read_log():
    try:
        read = open(logs_file, "rb") # rb = open the file to read Binary
        # read the Binary and convert it to the original object
        temp_list = pickle.load(reader)

        for log in temp_list:
            logs.append(log)

        print(" Loaded: " + str(len(temp_list)) + " log events")

    except:
        # you get here if try block crashes
        print(" *Error: Data could not be loaded")

def print_header(text):
    print("\n\n")
    print("*" * 40)
    print(text)
    print("*" * 40)

def print_all(header_text):
    print_header(header_text)
    print("-" * 70)
    print("ID | Item Title               | Category        |     Price  | Stock")  
    print("-" * 70)

    for item in items:
        print(str(item.id).ljust(3) + "| " + item.title.ljust(25) + "| " + item.category.ljust(15) + " |€ " + str(item.price).rjust(9) + " | " + str(item.stock).rjust(5))

def register_items():
    global id_count # importing the global variables, into fn scope

    print_header(" ----- Register New Product -----")
    title = input("Enter Title: ")
    category = input("Enter Category: ")
    price = float(input("Enter the Price: "))
    stock = int(input("Enter the Stock: "))

    # validations

    new_item = Item()
    new_item.id = id_count
    new_item.title = title
    new_item.category = category
    new_item.price = price
    new_item.stock = stock

    id_count += 1
    items.append(new_item)
    print(" Item Created")


def update_stock():

    print_all("Choose an Item form the list")
    id = input("\nSelect and ID & update Stock: ")

    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("Please input new stock value: ")
            item.stock = int(stock)
            found = True
            

            log_line = get_time() + " | Update | " + id
            logs.append(log_line)
            save_log()

    if(not found):
        print("** Error: ID does not Exist, Please re-try")

def remove_item():
    print_all("Chose an Item to remove")
    id = input("\nSelect and ID & Remove: ")

    for item in items:
        if(str(item.id) == id):
            items.remove(item)
            print(" Item has been removed")


def list_no_stock():
    print_header("Items With No Stock")
    for item in items:
        if(item.stock == 0):
            print(item.title)


def print_categories():
    temp_list = []

    for item in items:
        if(item.category not in temp_list):
            temp_list.append(item.category)

    print(temp_list)

def register_purchase():
    """
    Show the items
    ask the user to select 1
    ask for the quantity in the order (purchase)
    update the stock of the selected item

    """

    print_all("Select a Purchased Item")
    id = input("\nSelect an ID & Update Stock")

    found = False
    for item in items:
        if(str(item.id) == id):
            stock = input("Number of Items: ")
            item.stock += int(stock)
            found = True
    if(not found):
        print("** Error: ID does not exist, try again")

def register_sell():

    """
    Show the items
    ask the user to select 1
    ask for the quantity in the order (purchase)
    update the stock of the selected item
    """
    print_all("Choose an Item that you sold")
    id = input("\nSelect an ID to the update its stock: ")

    found = False 
    for item in items:
        if(str(item.id) == id):
            stock = input("Number of Items: ")
            item.stock -= int(stock)
            found = True
    if(not found):
        print("** Error: ID does not exist, try again")

def print_stock_value():
    total = 0.0
    for item in items:
        total += (item.price * float(item.stock))

    print("Total Stock Value: " + str(total))


read_items()
read_log()

opc = ''
while(opc != 'x'):
    clear()
    print_menu()

    opc = input("Please select an option: ")

    # actions based on selected opc
    if(opc == "1"):
        register_items()
        save_items()
    elif(opc == "2"):
        print_all("List of all Items")
    elif(opc == "3"):
        update_stock()
        save_items()
    elif(opc == "4"):
        list_no_stock()
    elif(opc == "5"):
        remove_item()
        save_items()
    
    elif(opc == "6"):
        print_categories()
    elif(opc == "7"):
        print_stock_value()
    elif(opc == "8"):
        register_purchase()
    elif(opc == "9"):
        register_sell()
    elif(opc == "10"):
        # print_log()
    
        if(opc != "x"):
            input("\n\nPress Enter to Continue...")





