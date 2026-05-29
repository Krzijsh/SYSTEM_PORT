# ==============================================================================
# FEATURE 5: VIEW RECORDS
# THIS FILE ACTS AS THE DIRECTORY. IT GRABS EVERYTHING FROM THE DATABASE 
# AND PRINTS IT ALL OUT INTO A LONG LIST SO STAFF CAN SEE THE DETAILS OF 
# EVERY SHIP EVER REGISTERED.
# ==============================================================================
import mysql.connector

class RecordViewer:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self):
        print("\n==========================================")
        print("               ALL RECORDS                ")
        print("==========================================")

        try:
            # GRAB ABSOLUTELY EVERYTHING FROM THE VESSELS TABLE
            self.cursor.execute("SELECT * FROM vessels")
            vessels = self.cursor.fetchall()

            if len(vessels) == 0:
                print(" ℹ️ No vessels recorded in the system.")
                print("==========================================")
            else:
                # LOOP THROUGH EVERY SHIP AND PRINT ITS INFORMATION NICELY
                for v in vessels:
                    v_id, v_name, v_type, capacity, current_load, status = v[0], v[1], v[2], v[3], v[4], v[5]
                    
                    # DECIDE WHAT WORD TO DISPLAY BASED ON THE SHIP TYPE
                    if v_type == "Passenger":
                        unit = "passengers"
                    else:
                        unit = "tons"

                    print(f" ID     : {v_id}")
                    print(f" Name   : {v_name}")
                    print(f" Type   : {v_type}")
                    print(f" Load   : {current_load} / {capacity} {unit}")
                    print(f" Status : {status}")

                    # AUTOMATICALLY FLAG SHIPS THAT ARE FULL
                    if current_load >= capacity:
                        print(" ⚠️ >> WARNING: MAX CAPACITY REACHED <<")
                    print("==========================================")
            
            input(" Press Enter to return to the main menu...")
            print()
            
        except mysql.connector.Error as err:
             print(f"\n🔴 Database Error: {err}")
             print("❌ Failed to fetch records.\n")

# ==============================================================================