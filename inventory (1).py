class Shoes():

    
    def __init__(self, country, code, product, cost, quantity):
       
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity
    
    
    def get_cost(self):
        return self.cost     # Return self.cost.
        
    
    def get_quantity(self):
        return self.quantity    # Return self.quantity.

    
    def __str__(self):
        # Return readable string in a table format
        return "{:<15} {:<15} {:<20} {:<15} {:<15}".format(self.country, 
                                                           self.code,
                                                           self.product, 
                                                           self.cost, 
                                                           self.quantity)


#=============Shoe list===========

shoe_object_list = []

#==========Functions outside the class==============


def read_shoes_data():
    """
    Adds shoe data to the list as objects
    """
    try:
        with open ('inventory.txt', 'r') as inventory_textfile:
            file = inventory_textfile.readlines()[1:]
            for row in file:  # Split it at the commas after its converted.
                row = row.replace('\n', '')
                row = row.split(',')

                # Create a shoe object which will be appendend to the list
                shoe = Shoes(row[0], row[1], row[2], row[3], row[4])
                shoe_object_list.append(shoe)
                
    except FileNotFoundError:
        print("File not found")

    
def capture_shoes():
    """
    Docstring for capture_shoes.
    """
    code_found = 1
    # Read data from textfile to list
    if len(shoe_object_list) == 0:
        read_shoes_data()
    # Ask for user inputs to append to list
    country = input("\u001b[36mPlease enter country: \u001b[37m")
    code = input("\u001b[36mPlease enter code in"
                 "format as follows 'SKU12345': \u001b[37m")
    product = input("\u001b[36mPlease enter product name: \u001b[37m")
    while True:
        try:
            cost = int(input("\u001b[36mPlease enter cost to nearest "
                             "whole number:\u001b[37m"))
            break
        except ValueError:
            print(" \u001b[31mOops! Invalid number, please try again.\u001b[37m")
            
    while True:
        try:
            quantity = int(input("\u001b[36mPlease enter quantity: \u001b[37m"))
            break
        except ValueError:
            print("\u001b[31mOops! Invalid number, please try again.\u001b[37m")
        
    # Create shoe object and append to list.
    shoe = Shoes(country, code, product, cost, quantity)
    shoe_object_list.append(shoe)
    
    try:
        with open ('inventory.txt', 'w') as inventory_textfile:
            for row in shoe_object_list:
                inventory_textfile.write(str(row.country) + "," + 
                str(row.code) + "," + str(row.product) + "," + str(row.cost) + 
                "," + str(row.quantity) + "\n")
            
            print("\u001b[36m\n\tNew shoe data added!\u001b[37m" + "\n")
    except FileNotFoundError:
            print("\u001b[31mFile not found\u001b[37m")


def view_all():
    """
    Docstring for view_all
    """
    # Shoe_object_list = []
    if len(shoe_object_list) == 0:
        read_shoes_data()   #read data from textfile to list
    # Loop through list and use str to convert objects to readable data
    # Print into a table format
    for row in shoe_object_list:
        shoe = Shoes(row.country, row.code, row.product, 
                     row.cost, row.quantity)
        print(shoe.__str__())
        
    print("\n")


def re_stock():
    """
    Docstring for re_stock
    """
    if len(shoe_object_list) == 0:
        read_shoes_data()
    
    min_num = int(shoe_object_list[1].quantity)
    index = 1
    
    for row, value in enumerate(shoe_object_list):
        if row == 0:
            continue
        
        value.quantity = int(value.quantity)
        
        if value.quantity < min_num:
        # Checking which number is smaller and assigning that number to min variable
            
            min_num = value.quantity
            index = row

    print(f"\u001b[36mLowest stock is:\u001b[37m {shoe_object_list[index].product}"
          f"Quantity: {shoe_object_list[index].quantity}\n")
    
    
    update_quantity = input("\u001b[36mWould you like to update the shoes"
                            "quantity 'yes' or 'no'? \u001b[37m").lower()
    
    if update_quantity == "yes":
    # If yes allow user to enter number to replinish with and add this number to list
    #write to textfile.
        
        while True:
            try:
                new_quantity = int(input("\u001b[36mWhat additional quantities"
                                         "would you like to add: \u001b[37m "))
                break
            except ValueError:
                print("\u001b[31mOops! Invalid number, please try again.\u001b[37m")
        new_total = shoe_object_list[index].quantity + new_quantity
        shoe_object_list[index].quantity = new_total
        try:
            with open ('inventory.txt', 'w') as inventory_textfile:
                for row in shoe_object_list:
                    inventory_textfile.write(str(row.country) + "," + 
                                             str(row.code) + "," + 
                                             str(row.product) + "," + 
                                             str(row.cost) + "," + 
                                             str(row.quantity) + "\n")
                
                print("\u001b[36m\n\tQuantity updated\u001b[37m" + "\n")
        except FileNotFoundError:
                print("\u001b[31mFile not found\u001b[37m")
    elif update_quantity == "no":   # If no quantity remains unchanged
        print("\u001b[31mQuantity unchanged\u001b[37m\n")
        
    else:
        print("\u001b[31mIncorrect input\u001b[37m\n")

    
def search_shoe():
    """
    Docstring for search_shoe
    """

    shoe_not_found = 0
    if len(shoe_object_list) == 0:
        read_shoes_data()
        
    # Program asks the user to type the code.
    shoe_search = input("\u001b[36mEnter SKU you are searching"
                        "for e.g.'SKU12345': \u001b[37m")
    x = 0
    for row in shoe_object_list:
        if x == 0:
            break
        print(f"\u001b[36m]{row}\u001b[37m]")
    x += 1
    for row in shoe_object_list:
        if shoe_search == row.code:
            return row
    else:
            shoe_not_found = 1  # If shoe is not found set variable to 1
    if shoe_not_found == 1:
        return "\u001b[31mShoe SKU not found!\u001b[37m"
    print("\n")
  
 
def value_per_item():
    """
    Docstring for value_per_item
    """

    if len(shoe_object_list) == 0:
        read_shoes_data()
    # Printing inital headings
    print("{:<15} {:<20} {:<15}".format("Code", "Product","Value"))
    for row, value in enumerate(shoe_object_list):
        if row == 0:    #don't check the first column with titles
            continue
        value.quantity = int(value.quantity)
        value.cost = int(value.cost)
        # Print values in table format
        print("{:<15} {:<20} R{:<15}".format(value.code, value.product, 
                                             value.quantity*value.cost))
    print("\n")


def highest_qty():
    """
    Docstring for highest_qty
    """

    if len(shoe_object_list) == 0:
        read_shoes_data()       # Read data from textfile to list
    max_num = int(shoe_object_list[1].quantity)
    index = 1
    for row, value in enumerate(shoe_object_list):
        if row == 0:
            continue
        value.quantity = int(value.quantity)
        # Checking which number is smaller and assigning that number to min variable
        if value.quantity > max_num:
            max_num = value.quantity
            index = row
    print(f"\u001b[36m{shoe_object_list[index].code}({shoe_object_list[index].product})"
          "is on SALE!!!\u001b[37m\n")


#==========Main Menu======================================================

print("\u001b[32m\n\t\tINVENTORY\n\u001b[37m")


def main():
    while True:
        # Presenting the menu to the user
        menu = input('''Select one of the following Options below:
        \u001b[36m1\u001b[37m - Add new shoe
        \u001b[36m2\u001b[37m - View all shoes
        \u001b[36m3\u001b[37m - Restock shoe with lowest quantity
        \u001b[36m4\u001b[37m - Search for by SKU code
        \u001b[36m5\u001b[37m - Stock on database value
        \u001b[36m6\u001b[37m - Shoe to sale
        \u001b[36m0\u001b[37m - Exit
        : \n\n''').lower()

        if menu == "1": # Add new shoe to database
            print("\u001b[36m\tAdd new shoe\u001b[37m\n")
            capture_shoes()
        elif menu == "2":   # View all shoes
            print("\u001b[36m\tView all shoes\u001b[37m\n")
            view_all()
        elif menu == "3":   # Restock shoe with lowest quantity
            print("\u001b[36m\tRestock shoe with lowest quantity\u001b[37m\n")
            re_stock()
        elif menu == "4":  # Search for a shoe
            print("\u001b[36m\tSearch for by SKU code\u001b[37m\n")
            print(f"\u001b[36m{search_shoe()} \u001b[37m\n")
        elif menu == "5":   # Get value of stock on hand
            print("\u001b[36m\tStock on database value\u001b[37m\n")
            value_per_item()
        elif menu == "6":   # Put a shoe on sale with highest quantity
            print("\u001b[36m\tShoe to sale\u001b[37m\n")
            highest_qty()
        elif menu == "0":   # Exit
            print("\u001b[36mGoodbye!\u001b[37m")
            exit()
        else:
            print("You have made a wrong choice, Please Try again!")

if __name__=="__main__":
    main()
