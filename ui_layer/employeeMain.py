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
                self.my_reports = self.wrapper.get_reports(self.id_num)
                self.my_reports_sorted = self.wrapper.sort_reports(self.my_reports)
                self.display_my_reports()
            
    def display_my_reports(self):
        self.clear_display()
        print(f"\033[96m{self.logo}\033[0m")
        print("\n")
        for report in self.my_reports:

            if len(report) == 5:
                work_order_id = report[0]
                work_done = report[1]
                additional_info = report[2]
                material_cost = report[3]
                total_cost = report[4]
                print(f"{work_order_id}, {work_done}, {additional_info}, {material_cost}, {total_cost}")
            else:
                work_order_id = report[0]
                work_done = report[1]
                contractor_name = report[2]
                contact_phone = report[3]
                contact_name = report[4]
                specialty = report[5]
                additional_info = report[6]
                material_cost = report[7]
                contractor_cost = report[8]
                total_cost = report[9]
                print(f"{work_order_id}, {work_done}, {contractor_name}, {contact_phone}, {contact_name}, {specialty}, {additional_info}, {material_cost}, {contractor_cost}, {total_cost}")
        input()


    def clear_display(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')