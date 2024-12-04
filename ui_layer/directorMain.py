class DirectorMain:

    def __init__(self, id_num, ll_wrapper):
        employee_info = ll_wrapper.getEmployee(id_num)
        self.job_title = employee_info[1]
        self.name = employee_info[0]

    def displayDirectorMain(self):
        print("\n")
        print("-" * 85)
        print("|",(self.name.ljust(33)), (self.job_title.rjust(47)), "|")
        print("-" * 85)
        print("|", "Employees".ljust(10), "|", "Contractors".ljust(10), "|", "Properties".ljust(10), "|", "Work-orders".ljust(10), "|", "My work-orders".ljust(10), "|", "My reports".ljust(10), "|")
        print("-" * 85)
        print("\n")

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