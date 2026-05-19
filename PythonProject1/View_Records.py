# ==============================================================================
# THIS FILE LETS US LOOK AT ALL THE SHIPS WE HAVE SAVED IN OUR SYSTEM. IT SHOWS 
# ALL THEIR DETAILS IN ONE BIG LIST.
# ==============================================================================

class RecordViewer:
    def __init__(self, cursor):
        self.cursor = cursor

    def execute(self):
        # ==============================================================================
        # WE GRAB EVERYTHING FROM THE DATABASE AND PRINT IT OUT LINE BY LINE SO 
        # WE CAN EASILY SEE WHAT IS GOING ON WITH EACH SHIP.
        # ==============================================================================
        print("\n==========================================")
        print("               ALL RECORDS                ")
        print("==========================================")

        self.cursor.execute("SELECT * FROM vessels")
        vessels = self.cursor.fetchall()

        if len(vessels) == 0:
            print(" ℹ️ No vessels recorded in the system.")
            print("==========================================\n")
        else:
            for v in vessels:
                v_id, v_name, v_type, capacity, current_load, status = v[0], v[1], v[2], v[3], v[4], v[5]

                print(f" ID     : {v_id}")
                print(f" Name   : {v_name}")
                print(f" Type   : {v_type}")
                print(f" Load   : {current_load} / {capacity}")
                print(f" Status : {status}")

                if current_load >= capacity:
                    print(" ⚠️ >> WARNING: MAX CAPACITY REACHED <<")
                print("==========================================")
        
        input("\n Press Enter to return to the main menu...")
        print("\n")

# ==============================================================================