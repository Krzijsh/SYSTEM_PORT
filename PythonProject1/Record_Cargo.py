# ==============================================================================
# FEATURE 2: RECORD CARGO / PASSENGERS
# THIS FILE UPDATES HOW MUCH CARGO OR HOW MANY PASSENGERS ARE CURRENTLY ON A SHIP.
# IT HAS A BUILT-IN SAFETY FEATURE: IT CHECKS THE SHIP'S MAXIMUM CAPACITY FIRST.
# IF THE NEW LOAD MAKES THE SHIP TOO HEAVY, IT BLOCKS THE ACTION.
# ==============================================================================
import mysql.connector

class CargoRecorder:
    def __init__(self, cursor, mydb):
        self.cursor = cursor
        self.mydb = mydb

    def execute(self):
        print("\n==========================================")
        print("               RECORD LOAD                ")
        print("==========================================")
        print(" 💡 Type '0' to return")
        print("==========================================")
        
        # ASK FOR THE VESSEL ID AND MAKE SURE THEY TYPE A NUMBER
        while True:
            v_id_input = input(" Enter Vessel ID: ").strip()
            
            if v_id_input == "0":
                print("\n ℹ️ Returning to main menu...\n")
                return
                
            if not v_id_input.isdigit():
                 print(" 📛 Invalid input! Vessel ID must be a number.")
                 continue
                 
            v_id = int(v_id_input)
            break

        try:
            # SEARCH THE DATABASE FOR THE SHIP THEY WANT TO LOAD
            self.cursor.execute("SELECT vessel_name, capacity, current_load, vessel_type, status FROM vessels WHERE id = %s", (v_id,))
            record = self.cursor.fetchone()

            # IF THE SHIP EXISTS IN THE DATABASE
            if record:
                v_name, capacity, current_load, v_type, status = record
                
                # WE CANNOT LOAD CARGO ONTO A SHIP THAT IS NO LONGER AT THE PORT
                if status == "Departed":
                    print("==========================================")
                    print(f"\n❌ Vessel '{v_name}' has already departed. Cannot record load.\n")
                    return

                print("==========================================")
                
                # SHOW THE CORRECT WORD (PASSENGERS OR TONS) BASED ON SHIP TYPE
                if v_type == "Passenger":
                    unit = "passengers"
                else:
                    unit = "tons"
                    
                print(f" Vessel: {v_name} ({v_type})")
                print(f" Current Load: {current_load} / {capacity} {unit}")
                print("==========================================")

                # KEEP ASKING HOW MUCH LOAD TO ADD UNTIL THEY GIVE A VALID NUMBER
                while True:
                    try:
                        if v_type == "Passenger":
                            load_prompt = " Enter number of passengers to add: "
                        else:
                            load_prompt = " Enter cargo in tons to add: "
                            
                        load_input = input(load_prompt).strip()
                        
                        if load_input == "0":
                            print("\n ℹ️ Returning to main menu...\n")
                            return
                            
                        added_load = int(load_input)
                        
                        if added_load < 0:
                            print(" 📛 Invalid input! Cannot add negative amounts.")
                            continue
                            
                        break
                    except ValueError:
                        print(f" 📛 Invalid input! Please enter a whole number.")

                print("==========================================")

                # SAFETY CHECK: MATH CALCULATION TO SEE IF IT EXCEEDS CAPACITY
                if current_load + added_load <= capacity:
                    new_load = current_load + added_load
                    
                    # UPDATE THE DATABASE WITH THE NEW TOTAL
                    self.cursor.execute("UPDATE vessels SET current_load = %s WHERE id = %s", (new_load, v_id))
                    self.mydb.commit()
                    print(f"\n✅ Load recorded! New load is {new_load}/{capacity} {unit}.\n")
                else:
                    # IF IT'S TOO HEAVY, BLOCK THE SAVE AND SHOW A WARNING
                    print(f"\n⚠️ Warning! Adding {added_load} exceeds the maximum capacity of {capacity} {unit}.")
                    print("⛔ Action denied for safety.\n")

            else:
                # THE ID THEY TYPED DOESN'T MATCH ANY SHIP IN THE DATABASE
                print("==========================================")
                print("\n❌ Vessel ID not found.\n")
                
        except mysql.connector.Error as err:
             print(f"\n🔴 Database Error: {err}")
             print("❌ Failed to read or update records.\n")

# ==============================================================================