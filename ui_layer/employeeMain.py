import os

class EmployeeMain:

    def __init__(self, id_number, ll_wrapper, logo):
        self.logo = logo
        self.id_num = id_number
        self.wrapper = ll_wrapper
        employee_info = self.wrapper.getEmployee(self.id_num)
        self.job_title = employee_info[1]
        self.name = employee_info[0]

    def displayEmployeeMain(self):

        print(f"\033[96m{self.logo}\033[0m")
        print("\n")
        print("-" * 100)
        print("|",(self.name.ljust(33)), (self.job_title.rjust(62)), "|")
        print("-" * 100)
        print("|", "My work-orders".ljust(45), "|", "My reports".ljust(48), "|")
        print("-" * 100, "\n")

        self.displayChoices()

    def displayChoices(self):
       
        choice = input("1) View my work-orders\n2) View my reports\n\nb) Back\n\n\nInput choice: ")

        while choice != "b":
        
            if choice != "1" and choice != "2":
                self.clear_display()
                print(f"\033[96m{self.logo}\033[0m")
                print("\n")
                print("-" * 100)
                print("|",(self.name.ljust(33)), (self.job_title.rjust(62)), "|")
                print("-" * 100)
                print("|", "My work-orders".ljust(45), "|", "My reports".ljust(48), "|")
                print("-" * 100, "\n")
                choice = input("1) View my work-orders\n2) View my reports\n\nb) Back\n\nInvalid choice, try again!\nInput choice: ")

            elif choice == "1":
                self.wrapper.get_work_orders(self.id_num)
            elif choice == "2":
                self.wrapper.get_reports(self.id_num)
            
           

    def clear_display(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')