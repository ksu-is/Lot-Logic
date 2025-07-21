# Global list to represent available parking spots
parking_spots = []

def add_parking_spot():
    new_spot = input("Enter the new parking spot ID to add: ").upper()
    if new_spot not in parking_spots:
        parking_spots.append(new_spot)
        print(f"Parking spot {new_spot} added successfully.")
    else:
        print(f"Parking spot {new_spot} is already in the system.")

def remove_parking_spot():
    spot_id = input("Enter the parking spot ID to remove: ").upper()
    if spot_id in parking_spots:
        parking_spots.remove(spot_id)
        print(f"Parking spot {spot_id} removed.")
    else:
        print(f"Parking spot {spot_id} not found.")

def view_parking_inventory():
    print("\nCurrent Available Parking Spots:")
    if parking_spots:
        for spot in parking_spots:
            print(f"- {spot}")
    else:
        print("No available parking spots at the moment.")

def lotlogic_menu():
    print("Welcome to LotLogic Smart Parking Tracker!\n")
    menu = {
        '1': "Add Parking Spot",
        '2': "Remove Parking Spot",
        '3': "View Parking Inventory",
        '4': "Exit"
    }

    while True:
        print("\nWhat would you like to do?")
        for key, value in menu.items():
            print(f"{key}. {value}")
        
        selection = input("Please select an option: ")
        if selection == '1':
            add_parking_spot()
        elif selection == '2':
            remove_parking_spot()
        elif selection == '3':
            view_parking_inventory()
        elif selection == '4':
            print("Exiting LotLogic. Goodbye!")
            break
        else:
            print("Unknown option selected. Please try again.")

# Start the application
lotlogic_menu()
