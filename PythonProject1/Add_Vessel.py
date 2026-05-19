# ==============================================================================
# THIS FILE HANDLES THE ADDING OF NEW SHIPS TO OUR SYSTEM. IT TAKES THE DETAILS
# LIKE THE NAME, TYPE, AND CAPACITY, AND SAVES IT INTO THE DATABASE.
# ==============================================================================

class VesselAdder:
    def __init__(self, cursor, mydb):
        self.cursor = cursor
        self.mydb = mydb

    def execute(self):
        # ==============================================================================
        # WE ASK THE USER FOR THE SHIP'S INFORMATION. ONCE WE HAVE IT, WE PUT IT
        # INTO A FORMAT OUR DATABASE UNDERSTANDS AND SAVE IT.
        # ==============================================================================
        print("\n==========================================")
        print("              ADD NEW VESSEL              ")
        print("==========================================")
        print(" 💡 Type '0' to return")
        print("==========================================")
        
        name = input(" Enter vessel name: ")
        
        if name.strip() == "0":
            print("\n ℹ️ Returning to main menu...\n")
            return

        v_type = input(" Enter vessel Type (Passengers/Cargo): ")
        
        if v_type.strip() == "0":
            print("\n ℹ️ Returning to main menu...\n")
            return

        try:
            capacity_input = input(" Enter maximum capacity: ")
            
            if capacity_input.strip() == "0":
                print("\n ℹ️ Returning to main menu...\n")
                return
                
            capacity = int(capacity_input)
            print("==========================================")
            
            sql = "INSERT INTO vessels (vessel_name, vessel_type, capacity, current_load, status) VALUES (%s, %s, %s, 0, 'Docked')"
            self.cursor.execute(sql, (name, v_type, capacity))
            self.mydb.commit()

            print(f"\n✅ Vessel '{name}' added successfully!\n")
        except ValueError:
            print("==========================================")
            print("\n📛 Invalid input! Capacity must be a number.\n")

# ==============================================================================