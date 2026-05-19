# ==============================================================================
# THIS FILE CREATES A QUICK SUMMARY OF WHAT IS HAPPENING AT THE PORT RIGHT NOW. 
# IT COUNTS THE SHIPS, CHECKS THEIR STATUS, AND LOOKS FOR SHIPS THAT ARE FULL.
# ==============================================================================

class ReportGenerator:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self):
        # ==============================================================================
        # WE PULL ALL THE INFO FROM THE DATABASE AND COUNT HOW MANY SHIPS WE HAVE, 
        # HOW MANY ARE DOCKED, HOW MANY HAVE LEFT, AND HOW MANY ARE COMPLETELY FULL.
        # ==============================================================================
        print("\n==========================================")
        print("          DAILY OPERATIONAL REPORT        ")
        print("==========================================")

        self.cursor.execute("SELECT capacity, current_load, status FROM vessels")
        vessels = self.cursor.fetchall()

        if len(vessels) == 0:
            print(" ℹ️ No records to generate a report.")
            print("==========================================\n")
        else:
            total_vessels = len(vessels)
            docked_count = 0
            departed_count = 0
            full_capacity_count = 0

            for v in vessels:
                capacity, current_load, status = v[0], v[1], v[2]

                if status == "Docked":
                    docked_count += 1
                if status == "Departed":
                    departed_count += 1
                if current_load >= capacity:
                    full_capacity_count += 1

            print(f" Total Vessels Tracked : {total_vessels}")
            print(f" Currently Docked      : {docked_count}")
            print(f" Currently Departed    : {departed_count}")
            print(f" Vessels at Max Load   : {full_capacity_count} ⚠️(Flagged)")
            print("==========================================\n")
            
        input("\n Press Enter to return to the main menu...")
        print("\n")

# ==============================================================================