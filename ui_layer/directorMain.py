import os
from prettytable import PrettyTable

class DirectorMain:

    def __init__(self, id_num, ll_wrapper):

        employee_info = ll_wrapper.getEmployee(id_num)
        self.job_title = employee_info[1]
        self.name = employee_info[0]


    def displayDirectorMain(self, blue_logo):

        self.blue_logo = blue_logo
        self.emp_main_display = PrettyTable(["Name", "Job title"])
        self.emp_main_display.add_row([self.name, self.job_title])

        print(self.blue_logo)
        print(f"\n{self.emp_main_display}\n")

        self.displayChoices()

        return "b"


    def displayChoices(self):

        choice = input("1) View all employees\n2) View all contractors\n3) View all properties\n4) View all work-orders\n5) View my work-orders\n6) View my reports\n\nq) Quit\n\nInput choice: ")


    def backToChoice(): #Sama fall til í employeeMain, skoða það
        pass


    def viewMyWorkOrders(): #Sama fall til í employeeMain, skoða það
        pass


    def viewMyReports(): #Sama fall til í employeeMain, skoða það
        pass


    def viewEmployees():
        pass


    def viewProperties():
        pass


    def viewContracters():
        pass


    def viewWorkOrders():
        pass


    def clear_display(self) -> None:
        
        os.system('cls' if os.name == 'nt' else 'clear')