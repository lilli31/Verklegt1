from employeeMain import EmployeeMain
from directorMain import DirectorMain

class MainMenu:

    def __init__(self):
        """ displays the main menu and takes in the users interface choice """

        self.displayLogo()
        self.choice = input("1) Employee\n2) Director\nq) Quit\n\nSign in as: ")
        
        while self.choice != "q":
            if self.choice == "1":
                EmployeeMain()
            elif self.choice == "2":
                DirectorMain()
            else:
                print("\nInvalid choice, try again!\n")
                self.choice = input("1) Employee\n2) Director\n\nSign in as: ")

    def displayLogo(self):
        """ prints a formatted string of the logo """

        print(f"""
                                ▗▖  ▗▖ ▗▄▖ ▗▖  ▗▖     ▗▄▖ ▗▄▄▄▖▗▄▄▖     
               __!__            ▐▛▚▖▐▌▐▌ ▐▌▐▛▚▖▐▌    ▐▌ ▐▌  █  ▐▌ ▐▌            ,____,
         ^----o-(_)-o----^      ▐▌ ▝▜▌▐▛▀▜▌▐▌ ▝▜▌    ▐▛▀▜▌  █  ▐▛▀▚▖           /__\___\    
                " "             ▐▌  ▐▌▐▌ ▐▌▐▌  ▐▌    ▐▌ ▐▌▗▄█▄▖▐▌ ▐▌           |__|___|      
              """)

    # def ChooseEmployee(self):
    #     pass

    # def ChooseDirector(self):
    #     pass