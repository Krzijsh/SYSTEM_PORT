# ==============================================================================
#  __  __  _____  _   _  _   _ 
#  \ \/ / | ____|| \ | || \ | |
#   \  /  |  _|  |  \| ||  \| |
#   /  \  | |___ | |\  || |\  |
#  /_/\_\ |_____||_| \_||_| \_|
#
# ==============================================================================

# ==============================================================================
# IMPORTING THE TOOLS AND BLUEPRINTS WE NEED TO MAKE THE SYSTEM WORK. 
# THIS INCLUDES THE DATABASE CONNECTOR AND THE DIFFERENT FEATURES LIKE 
# ADDING VESSELS OR RECORDING CARGO.
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
        # SETTING UP THE SYSTEM. WE TRY TO CONNECT TO OUR DATABASE WHERE ALL THE 
        # INFORMATION IS STORED. IF IT WORKS, WE PREPARE ALL OUR FEATURES. IF NOT, 
        # WE SHOW AN ERROR AND STOP THE PROGRAM.
        # ==============================================================================
        print("⏳ Connecting to database...")
        time.sleep(1.5)

        try:
            self.mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="port_system"
            )
            self.cursor = self.mydb.cursor()
            print("✅ Connected successfully!\n")
            time.sleep(1.5)

            # pass the database connection to them so they can do their jobs
            self.adder = VesselAdder(self.cursor, self.mydb)
            self.recorder = CargoRecorder(self.cursor, self.mydb)
            self.updater = StatusUpdater(self.cursor, self.mydb)
            self.reporter = ReportGenerator(self.cursor)
            self.viewer = RecordViewer(self.cursor)

        except mysql.connector.Error:
            print(f"\n🔴 Could not connect to the database.")
            print("💡 Please make sure XAMPP is running and the 'port_system' database exists.")
            sys.exit()

    def run_menu(self):
        # ==============================================================================
        # THIS IS THE MAIN MENU THAT SHOWS UP ON THE SCREEN. IT ASKS THE USER WHAT 
        # THEY WANT TO DO AND WAITS FOR THEIR CHOICE. BASED ON THEIR NUMBER, IT 
        # OPENS THE RIGHT FEATURE.
        # ==============================================================================
        while True:
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

    def exit_system(self):
        # ==============================================================================
        # THIS CHECKS IF THE USER REALLY WANTS TO LEAVE. IF THEY SAY YES, WE SAFELY 
        # CLOSE THE CONNECTION TO THE DATABASE AND TURN OFF THE PROGRAM.
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
# THIS IS THE STARTING POINT OF OUR PROGRAM. IT CREATES THE SYSTEM AND 
# LAUNCHES THE MAIN MENU FOR THE USER.
# ==============================================================================
if __name__ == "__main__":
    app = PortSystem()
    app.run_menu()
