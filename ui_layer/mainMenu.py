from ui_layer.employeeMain import EmployeeMain
from ui_layer.directorMain import DirectorMain
from logic_layer.LL_wrapper import LogicLayerWrapper
import os

class MainMenu:

    def __init__(self):
        """ displays the main menu """

        self.logo = f"""
                                ▗▖  ▗▖ ▗▄▖ ▗▖  ▗▖     ▗▄▖ ▗▄▄▄▖▗▄▄▖     
               __!__            ▐▛▚▖▐▌▐▌ ▐▌▐▛▚▖▐▌    ▐▌ ▐▌  █  ▐▌ ▐▌            ,____,
         ^----o-(_)-o----^      ▐▌ ▝▜▌▐▛▀▜▌▐▌ ▝▜▌    ▐▛▀▜▌  █  ▐▛▀▚▖           /__\___\    
                " "             ▐▌  ▐▌▐▌ ▐▌▐▌  ▐▌    ▐▌ ▐▌▗▄█▄▖▐▌ ▐▌           |__|___|      
              """
        self.logic_layer_wrapper = LogicLayerWrapper()
        self.employee_main = EmployeeMain(9, self.logic_layer_wrapper, self.logo)
        self.director_main = DirectorMain(13, self.logic_layer_wrapper)
        #self.main = MainMenu()

        self.displayLogo()
        self.displayChoice() 
        

    def displayLogo(self):
        """ prints a formatted string of the logo """

        self.clear_display()
        self.BLUE = f"\033[96m{self.logo}\033[0m"

        print(self.BLUE)
        
        
    def displayChoice(self):
        """ displays the user interface choice """

        self.choice = "m"
        # while self.choice == "m":
        #     self.choice = input("1) Employee\n2) Director\n\nq) Quit\n\n\nSign in as: ")
            
        while self.choice != "q":
            if self.choice == "1":
                self.clear_display()
                self.employee_main.displayEmployeeMain()
                self.choice = "m"
            elif self.choice == "2":
                self.clear_display()
                self.director_main.displayDirectorMain(self.logo)
                self.choice = "m"
            elif self.choice == "m":
                self.clear_display()
                print(self.BLUE)
                self.choice = input("1) Employee\n2) Director\n\nq) Quit\n\n\nSign in as: ")
            elif self.choice != "m" and self.choice != "1" and self.choice != "2":
                self.clear_display()
                print(self.BLUE)
                self.choice = input("1) Employee\n2) Director\n\nq) Quit\n\nInvalid choice, try again!\nSign in as: ")

    def clear_display(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')