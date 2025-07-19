# Global list to represent available parking spots
parking_spots = []

def add_parking_spot():
    new_spot = input("Enter the new parking spot ID to add: ").upper()
    if new_spot not in parking_spots:
        parking_spots.append(new_spot)
        print(f"Parking spot {new_spot} added successfully.")
    else:
        print(f"Parking spot {new_spot} is already in the system.")
# fix the rest from here 
def remove_vehicle():
    global vehicle_list2
    
    removal = input("Do you know the ID for the Vehicle to remove? ")
    if removal == "no":
            print(vehicle_list)
            removal = input("Input Id for vehicle:")
    else:
        Id_search = [word for word in vehicle_list if word in removal]
        print(Id_search)
        vehicle_list.remove(new_ID)
    

    print(vehicle_list)


def print_inventory():
     global vehicle_list
     print(vehicle_list)

def opening_menu():
     print("Welcome to J&J Car Tracker! What would you like to do?")
     menu = {}
     menu ['1'] = "Add Vehicle"
     menu ['2'] = "Remove Vehicle"
     menu ['3'] = "Find Vehicle ID"
     menu ['4'] = "Exit"
     while True: 
        options=menu.keys()
        for entry in options: 
             print (entry, menu[entry])

        selection = input("Please Select:") 
        if selection =='1': 
            add_vehicle() 
        elif selection == '2': 
            remove_vehicle()
        elif selection == '3':
            print_inventory()
        elif selection == '4': 
            break
        else: 
            print ("Unknown Option Selected!")
# Try to fix for lot Logic use
opening_menu()
