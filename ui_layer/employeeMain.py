

class EmployeeMain:

    def __init__(self, id_number, ll_wrapper):
        #self.id_number = id_number
        employee_info = ll_wrapper.getEmployee(id_number)
        self.job_title = employee_info[1]
        self.name = employee_info[0]
        #self.displayEmployeeMain()

    def displayEmployeeMain(self):
        print("\n")
        print("-" * 70)
        print("|",(self.name.ljust(33)), (self.job_title.rjust(32)), "|")
        print("-" * 70)
        print("|", "My work-orders".ljust(30), "|", "My reports".ljust(33), "|")
        print("-" * 70, "\n")
        self.displayChoices()

    def displayChoices(self):
        choice = input("1) View my work-orders\n2) View my reports\n\nq) Quit\n\nInput choice: ")