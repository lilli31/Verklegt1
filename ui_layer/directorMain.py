import os
from prettytable import PrettyTable

class DirectorMain:

    def __init__(self, id_num, ll_wrapper):

        self.id_num = id_num
        self.ll_wrapper = ll_wrapper
        employee_info = self.ll_wrapper.getEmployee(id_num)
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

        choice = input("1) View all employees\n2) View all contractors\n3) View all properties\n4) View all work-orders\n5) View my work-orders\n6) View my reports\n\nb) Back\n\n\nInput choice: ")

        while choice != "b": # b will go back to the main menu interface
            if choice != "1" and choice != "2" and choice != "3" and choice != "4" and choice != "5" and choice != "6":
                pass
            elif choice == "1":
                pass
            elif choice == "2":
                pass
            elif choice == "3":
                pass
            elif choice == "4":
                pass
            elif choice == "5":
                pass
            elif choice == "6":
                self.my_reports = self.ll_wrapper.get_reports(self.id_num)
                exiting = self.display_my_reports()
                input()

    def display_my_reports(self):

        self.clear_display()
        print(f"\033[96m{self.blue_logo}\033[0m")
        print("\n")
        report_display_no_contractor = PrettyTable(["Work done", "Additional info", "Cost of material", "Total cost"])
        report_display_contractor = PrettyTable(["Work done", "Contractor", "Contractor specialty", "Contact contractor", "Additional info", "Cost of material", "Contractors commission", "Total cost"])

        for report in self.my_reports: # Breyta í sorted þegar búið er að útfæra

            if len(report) == 5:

                work_done = report[1]
                additional_info = report[2]
                material_cost = report[3]
                total_cost = report[4]

                report_display_no_contractor.add_row([work_done, additional_info, material_cost, total_cost])
                print(f"{report_display_no_contractor}\n")
                report_display_no_contractor.del_row(0)

            else:
                
                work_done = report[1]
                contractor_name = report[2]
                contact_phone = report[3]
                contact_name = report[4]
                specialty = report[5]
                additional_info = report[6]
                material_cost = report[7]
                contractor_cost = report[8]
                total_cost = report[9]

                report_display_contractor.add_row([work_done, contractor_name, specialty, (contact_name + ": " + contact_phone), additional_info, material_cost, contractor_cost, total_cost])
                print(f"{report_display_contractor}\n")
                report_display_contractor.del_row(0)

        input("Enter 'x' to exit my reports: ")

        return "x"


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