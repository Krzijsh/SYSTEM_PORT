# ==============================================================================
# FEATURE 3: UPDATE STATUS
# THIS FILE CHANGES THE LOCATION STATUS OF A SHIP. 
# IT LETS THE PORT STAFF MARK A SHIP AS "DOCKED" (CURRENTLY HERE) 
# OR "DEPARTED" (HAS LEFT THE PORT).
# ==============================================================================
import mysql.connector

class StatusUpdater:
    def __init__(self, cursor, mydb):
        self.cursor = cursor
        self.mydb = mydb

    def execute(self):
        print("\n==========================================")
        print("              UPDATE STATUS               ")
        print("==========================================")
        print(" 💡 Type '0' to return")
        print("==========================================")
        
        # ASK FOR THE VESSEL ID AND ENSURE IT'S A NUMBER
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
            # LOOK UP THE CURRENT STATUS OF THE SHIP
            self.cursor.execute("SELECT status FROM vessels WHERE id = %s", (v_id,))
            record = self.cursor.fetchone()

            if record:
                print("==========================================")
                print(f" Current Status: {record[0]}")
                print("==========================================")
                print(" [1] Docked (Arrival)")
                print(" [2] Departed (Departure)")
                print("==========================================")
                
                # ASK WHAT THE NEW STATUS SHOULD BE
                while True:
                    choice = input(" Select new status (1 or 2): ").strip()
                    
                    if choice == "0":
                        print("\n ℹ️ Returning to main menu...\n")
                        return
                    elif choice == "1":
                        new_status = "Docked"
                        break
                    elif choice == "2":
                        new_status = "Departed"
                        break
                    else:
                        print(" 📛 Invalid choice. Please press 1 or 2.")
                        
                print("==========================================")
                
                # CHECK IF IT'S ALREADY THE SELECTED STATUS SO WE DON'T DO USELESS WORK
                if record[0] == new_status:
                     print(f"\n ℹ️ Status is already set to {new_status}.\n")
                else:
                    # UPDATE THE DATABASE
                    self.cursor.execute("UPDATE vessels SET status = %s WHERE id = %s", (new_status, v_id))
                    self.mydb.commit()
                    print(f"\n✅ Status updated to: {new_status}\n")

            else:
                print("==========================================")
                print("\n❌ Vessel ID not found.\n")
                
        except mysql.connector.Error as err:
             print(f"\n🔴 Database Error: {err}")
             print("❌ Failed to read or update status.\n")

# ==============================================================================