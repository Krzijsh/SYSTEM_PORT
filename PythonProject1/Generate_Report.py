# ==============================================================================
# FEATURE 4: GENERATE DAILY REPORT
# THIS FILE IS AN ANALYTICS TOOL. IT LOOKS AT ALL THE SHIPS CURRENTLY IN THE 
# DATABASE AND COUNTS THEM UP TO CREATE A QUICK, EASY-TO-READ DASHBOARD SUMMARY.
# ==============================================================================
import mysql.connector

class ReportGenerator:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self):
        print("\n==========================================")
        print("          DAILY OPERATIONAL REPORT        ")
        print("==========================================")

        try:
            # GRAB THE SPECIFIC COLUMNS WE NEED FROM EVERY SINGLE SHIP
            self.cursor.execute("SELECT capacity, current_load, status FROM vessels")
            vessels = self.cursor.fetchall()

            if len(vessels) == 0:
                print(" ℹ️ No records to generate a report.")
                print("==========================================")
            else:
                total_vessels = len(vessels)
                docked_count = 0
                departed_count = 0
                full_capacity_count = 0

                # LOOP THROUGH EVERY SHIP ONE BY ONE AND UPDATE OUR COUNTERS
                for v in vessels:
                    capacity, current_load, status = v[0], v[1], v[2]

                    if status == "Docked":
                        docked_count += 1
                    if status == "Departed":
                        departed_count += 1
                        
                    # IF A SHIP IS 100% FULL, ADD IT TO THE WARNING COUNT
                    if current_load >= capacity:
                        full_capacity_count += 1

                # PRINT OUT THE FINAL TALLIED NUMBERS
                print(f" Total Vessels Tracked : {total_vessels}")
                print(f" Currently Docked      : {docked_count}")
                print(f" Currently Departed    : {departed_count}")
                print("==========================================")
                
            input(" Press Enter to return to the main menu...")
            print()
            
        except mysql.connector.Error as err:
             print(f"\n🔴 Database Error: {err}")
             print("❌ Failed to generate report.\n")

# ==============================================================================