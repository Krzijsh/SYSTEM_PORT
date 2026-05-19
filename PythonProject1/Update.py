# ==============================================================================
# THIS FILE IS USED TO CHANGE THE STATUS OF A SHIP, LIKE IF IT HAS ARRIVED AT 
# THE PORT (DOCKED) OR IF IT HAS LEFT (DEPARTED).
# ==============================================================================

class StatusUpdater:
    def __init__(self, cursor, mydb):
        self.cursor = cursor
        self.mydb = mydb

    def execute(self):
        # ==============================================================================
        # WE FIND THE SHIP USING ITS ID, SHOW ITS CURRENT STATUS, AND ASK THE USER 
        # IF IT IS NOW DOCKED OR DEPARTED. WE THEN UPDATE THIS INFO IN THE DATABASE.
        # ==============================================================================
        print("\n==========================================")
        print("              UPDATE STATUS               ")
        print("==========================================")
        print(" 💡 Type '0' to return")
        print("==========================================")
        
        v_id = input(" Enter Vessel ID: ")
        
        if v_id.strip() == "0":
            print("\n ℹ️ Returning to main menu...\n")
            return

        self.cursor.execute("SELECT status FROM vessels WHERE id = %s", (v_id,))
        record = self.cursor.fetchone()

        if record:
            print("==========================================")
            print(f" Current Status: {record[0]}")
            print("==========================================")
            print(" [1] Docked (Arrival)")
            print(" [2] Departed (Departure)")
            print("==========================================")
            
            choice = input(" Select new status (1 or 2): ")
            print("==========================================")

            if choice == "1":
                self.cursor.execute("UPDATE vessels SET status = 'Docked' WHERE id = %s", (v_id,))
                self.mydb.commit()
                print(f"\n✅ Status updated to: Docked\n")
            elif choice == "2":
                self.cursor.execute("UPDATE vessels SET status = 'Departed' WHERE id = %s", (v_id,))
                self.mydb.commit()
                print(f"\n✅ Status updated to: Departed\n")
            elif choice == "0":
                print("\n ℹ️ Returning to main menu...\n")
                return
            else:
                print("\n📛 Invalid choice. Please press 1 or 2.\n")
        else:
            print("==========================================")
            print("\n❌ Vessel ID not found.\n")

# ==============================================================================