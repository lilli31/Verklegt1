from logic_layer.LL_wrapper import LogicLayerWrapper


class EmployeeMain:

    def __init__(self, id_number):
        self.id_number = id_number
        self.ll_instance = LogicLayerWrapper()
        self.employee_info = self.ll_instance.getEmployee(self.id_number)
        self.job_title = self.employee_info[0]
        self.name = self.employee_info[1]
        self.displayEmployeeMain()

    def displayEmployeeMain(self):
        print("\n", ("-" * 70))
        print("|",(self.name.ljust(33)), (self.job_title.rjust(32)), "|")
        print("-" * 70)

    def backToChoice(self):
        pass

    def viewMyWorkOrders(self):
        pass

    def viewMyReports(self):
        pass