# ==============================================================================
# THIS FILE HELPS US KEEP TRACK OF HOW MUCH CARGO OR HOW MANY PASSENGERS
# ARE GETTING ON A SPECIFIC SHIP. IT ALSO MAKES SURE WE DON'T OVERLOAD IT.
# ==============================================================================

class CargoRecorder:
    def __init__(self, cursor, mydb):
        self.cursor = cursor
        self.mydb = mydb

    def execute(self):
        # ==============================================================================
        # WE ASK FOR THE SHIP'S ID, LOOK IT UP, AND SEE HOW MUCH STUFF IT CAN STILL 
        # CARRY. IF THE NEW LOAD FITS, WE UPDATE THE DATABASE. IF IT'S TOO MUCH, 
        # WE BLOCK IT TO KEEP EVERYONE SAFE.
        # ==============================================================================
        print("\n==========================================")
        print("               RECORD LOAD                ")
        print("==========================================")
        print(" 💡 Type '0' to return")
        print("==========================================")
        
        v_id = input(" Enter Vessel ID: ")
        
        if v_id.strip() == "0":
            print("\n ℹ️ Returning to main menu...\n")
            return

        self.cursor.execute("SELECT vessel_name, capacity, current_load FROM vessels WHERE id = %s", (v_id,))
        record = self.cursor.fetchone()

        if record:
            v_name, capacity, current_load = record

            print("==========================================")
            print(f" Vessel: {v_name} | Current Load: {current_load} / {capacity}")
            print("==========================================")

            try:
                load_input = input(" Enter cargo weight or passenger count to add: ")
                
                if load_input.strip() == "0":
                    print("\n ℹ️ Returning to main menu...\n")
                    return
                    
                added_load = int(load_input)
                print("==========================================")

                if current_load + added_load <= capacity:
                    new_load = current_load + added_load
                    self.cursor.execute("UPDATE vessels SET current_load = %s WHERE id = %s", (new_load, v_id))
                    self.mydb.commit()
                    print(f"\n✅ Load recorded! New load is {new_load}/{capacity}.\n")
                else:
                    print(f"\n⚠️ Warning! Adding {added_load} exceeds the maximum capacity of {capacity}.")
                    print("⛔ Action denied for safety.\n")

            except ValueError:
                print("==========================================")
                print("\n📛 Invalid input! Load amount must be a number.\n")
        else:
            print("==========================================")
            print("\n❌ Vessel ID not found.\n")

# ==============================================================================