# ==============================================================================
#  __  __  _____  _   _  _   _ 
#  \ \/ / | ____|| \ | || \ | |
#   \  /  |  _|  |  \| ||  \| |
#   /  \  | |___ | |\  || |\  |
#  /_/\_\ |_____||_| \_||_| \_|
#
# ==============================================================================

# ==============================================================================
# STEP 1: IMPORT THE NECESSARY TOOLS
# WE NEED 'SYS' AND 'TIME' FOR SYSTEM ACTIONS, AND 'MYSQL.CONNECTOR' TO TALK 
# TO OUR DATABASE. WE ALSO BRING IN ALL OUR CUSTOM FEATURES FROM THE OTHER FILES.
# ==============================================================================
import sys
import time

import mysql.connector

from Add_Vessel import VesselAdder
from Generate_Report import ReportGenerator
from Record_Cargo import CargoRecorder
from Update import StatusUpdater
from View_Records import RecordViewer


class PortSystem:
    def __init__(self):
        # ==============================================================================
        # STEP 2: CONNECT TO THE DATABASE
        # WHEN THE PROGRAM STARTS, IT TRIES TO CONNECT TO OUR MYSQL DATABASE.
        # IF IT CONNECTS, IT PREPARES ALL OUR FEATURES (ADDING, UPDATING, ETC.) 
        # SO THEY ARE READY TO USE. IF IT FAILS, IT SHOWS AN ERROR AND STOPS.
        # ==============================================================================
        print("⏳ Connecting to database...")

        try:
            time.sleep(1.5)
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="port_system"
            )
            self.cursor = self.mydb.cursor()
            print("✅ Connected successfully!\n")
            time.sleep(1.5)

            # PASS THE DATABASE CONNECTION TO OUR TOOLS SO THEY CAN SAVE/READ DATA
            self.adder = VesselAdder(self.cursor, self.mydb)
            self.recorder = CargoRecorder(self.cursor, self.mydb)
            self.updater = StatusUpdater(self.cursor, self.mydb)
            self.reporter = ReportGenerator(self.cursor)
            self.viewer = RecordViewer(self.cursor)

        except mysql.connector.Error:
            print(f"\n🔴 Could not connect to the database.")
            print("💡 Please make sure XAMPP is running and the 'port_system' database exists.")
            sys.exit()
        except KeyboardInterrupt:
            print("\n\n🛑 Force quitting the system during connection. Goodbye!\n")
            sys.exit()

    def run_menu(self):
        # ==============================================================================
        # STEP 3: THE MAIN MENU LOOP
        # THIS IS WHAT THE USER SEES. IT KEEPS REPEATING UNTIL THE USER CHOOSES TO EXIT.
        # BASED ON THE NUMBER THEY TYPE, IT OPENS THE CORRECT FEATURE.
        # ==============================================================================
        while True:
            try:
                print("==========================================")
                print("          PORT OF MANILA SYSTEM           ")
                print("==========================================")
                print(" [1] Add Vessel")
                print(" [2] Record Cargo and Passengers")
                print(" [3] Update Arrival and Departure")
                print(" [4] Generate Daily Report")
                print(" [5] View Records")
                print(" [6] Exit")
                print("==========================================")

                choice = input(" Please Enter Your Choice: ")
                print("==========================================")

                match choice:
                    case "1":
                        self.adder.execute()
                    case "2":
                        self.recorder.execute()
                    case "3":
                        self.updater.execute()
                    case "4":
                        self.reporter.execute()
                    case "5":
                        self.viewer.execute()
                    case "6":
                        self.exit_system()
                    case _:
                        print("\n📛 Invalid choice! Please select a number from 1 to 6.\n")
            
            except KeyboardInterrupt:
                # IF THE USER PRESSES CTRL+C, STOP THE PROGRAM SAFELY
                print("\n\n🛑 Force quitting the system. Goodbye!\n")
                if hasattr(self, 'mydb') and self.mydb.is_connected():
                    self.cursor.close()
                    self.mydb.close()
                sys.exit()

    def exit_system(self):
        # ==============================================================================
        # STEP 4: SAFE EXIT
        # WHEN EXITING, WE CONFIRM THEIR CHOICE. IF YES, WE DISCONNECT FROM THE 
        # DATABASE SAFELY SO NO DATA GETS CORRUPTED, THEN TURN OFF THE PROGRAM.
        # ==============================================================================
        print("\n==========================================")
        confirm = input(" Are you sure you want to exit? (Yes/No): ").strip().lower()
        print("==========================================")
        if confirm in ["yes", "y"]:
            print("🛑 Exiting Port of Manila System... Goodbye!")
            if self.mydb.is_connected():
                self.cursor.close()
                self.mydb.close()
            sys.exit()
        else:
            print("ℹ️ Exit cancelled. Returning to menu...\n")


# ==============================================================================
# HOW THE PROGRAM STARTS
# THIS TINY BLOCK AT THE BOTTOM CREATES OUR SYSTEM AND TURNS ON THE MENU.
# ==============================================================================
if __name__ == "__main__":
    try:
        app = PortSystem()
        app.run_menu()
    except KeyboardInterrupt:
        pass
