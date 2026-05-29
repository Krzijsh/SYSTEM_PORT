# ==============================================================================
# FEATURE 1: ADD VESSEL
# THIS FILE HANDLES REGISTERING A NEW SHIP INTO THE PORT'S DATABASE.
# IT ASKS THE USER FOR THE SHIP'S NAME, WHETHER IT CARRIES PASSENGERS OR CARGO, 
# AND HOW MUCH IT CAN CARRY. FINALLY, IT SAVES THIS INFO TO THE DATABASE.
# ==============================================================================
import mysql.connector

class VesselAdder:
    def __init__(self, cursor, mydb):
        self.cursor = cursor
        self.mydb = mydb

    def execute(self):
        print("\n==========================================")
        print("              ADD NEW VESSEL              ")
        print("==========================================")
        print(" 💡 Type '0' to return")
        print("==========================================")
        
        # KEEP ASKING FOR A NAME UNTIL THEY GIVE A VALID ONE
        while True:
            name = input(" Enter vessel name: ").strip()
            if name == "0":
                print("\n ℹ️ Returning to main menu...\n")
                return
            if name == "":
                print(" 📛 Vessel name cannot be empty. Please try again.")
            else:
                break

        # KEEP ASKING FOR A TYPE UNTIL THEY TYPE "PASSENGER" OR "CARGO"
        while True:
            v_type_input = input(" Enter vessel Type (Passenger/Cargo): ").strip()
            
            if v_type_input == "0":
                print("\n ℹ️ Returning to main menu...\n")
                return
            
            if v_type_input.lower() in ["passenger", "passengers"]:
                v_type = "Passenger"
                capacity_prompt = " Enter max capacity (number of passengers): "
                break
            elif v_type_input.lower() == "cargo":
                v_type = "Cargo"
                capacity_prompt = " Enter max capacity (in tons): "
                break
            else:
                print(" 📛 Invalid type! Please type 'Passenger' or 'Cargo'.")

        # KEEP ASKING FOR CAPACITY UNTIL THEY TYPE A VALID NUMBER
        while True:
            try:
                capacity_input = input(capacity_prompt).strip()
                
                if capacity_input == "0":
                    print("\n ℹ️ Returning to main menu...\n")
                    return
                    
                capacity = int(capacity_input)
                
                if capacity <= 0:
                    print(" 📛 Capacity must be greater than 0. Please try again.")
                    continue
                    
                break
            except ValueError:
                # IF THEY TYPED LETTERS INSTEAD OF NUMBERS, CATCH THE ERROR HERE
                print(" 📛 Invalid input! Capacity must be a whole number.")

        print("==========================================")
        
        # TRY TO SAVE THE NEW SHIP TO THE DATABASE. IF XAMPP CRASHES, CATCH THE ERROR.
        try:
            sql = "INSERT INTO vessels (vessel_name, vessel_type, capacity, current_load, status) VALUES (%s, %s, %s, 0, 'Docked')"
            self.cursor.execute(sql, (name, v_type, capacity))
            self.mydb.commit()

            print(f"\n✅ Vessel '{name}' added successfully!\n")
        except mysql.connector.Error as err:
            print(f"\n🔴 Database Error: {err}")
            print("❌ Failed to add vessel.\n")

# ==============================================================================