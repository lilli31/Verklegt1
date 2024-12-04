

class EmployeeMain:

    def __init__(self, id_number, ll_wrapper):
        #self.id_number = id_number
        employee_info = ll_wrapper.getEmployee(id_number)
        self.job_title = employee_info[1]
        self.name = employee_info[0]
        #self.displayEmployeeMain()

    def displayEmployeeMain(self, logo):
        print(f"\033[96m{logo}\033[0m")
        print("\n")
        print("-" * 100)
        print("|",(self.name.ljust(33)), (self.job_title.rjust(62)), "|")
        print("-" * 100)
        print("|", "My work-orders".ljust(45), "|", "My reports".ljust(48), "|")
        print("-" * 100, "\n")
        self.displayChoices()

    def displayChoices(self):
        choice = input("1) View my work-orders\n2) View my reports\n\nq) Quit\n\nInput choice: ")
        