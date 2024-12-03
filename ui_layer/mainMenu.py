from ui_layer.employeeMain import EmployeeMain
from ui_layer.directorMain import DirectorMain

class MainMenu:

    def __init__(self):
        """ displays the main menu """

        self.displayLogo()
        self.displayChoice() 

    def displayLogo(self):
        """ prints a formatted string of the logo """

        print(f"""
                                ▗▖  ▗▖ ▗▄▖ ▗▖  ▗▖     ▗▄▖ ▗▄▄▄▖▗▄▄▖     
               __!__            ▐▛▚▖▐▌▐▌ ▐▌▐▛▚▖▐▌    ▐▌ ▐▌  █  ▐▌ ▐▌            ,____,
         ^----o-(_)-o----^      ▐▌ ▝▜▌▐▛▀▜▌▐▌ ▝▜▌    ▐▛▀▜▌  █  ▐▛▀▚▖           /__\___\    
                " "             ▐▌  ▐▌▐▌ ▐▌▐▌  ▐▌    ▐▌ ▐▌▗▄█▄▖▐▌ ▐▌           |__|___|      
              """)
        
    def displayChoice(self):
        """ displays the user interface choice """

        self.choice = input("1) Employee\n2) Director\nq) Quit\n\nSign in as: ")
        
        while self.choice != "q":
            if self.choice == "1":
                EmployeeMain(19)
                self.choice = "q" #Fyrir test
            elif self.choice == "2":
                DirectorMain()
                self.choice = "q" #Fyrir test
            else:
                print("\nInvalid choice, try again!\n")
                self.choice = input("1) Employee\n2) Director\n\nSign in as: ")