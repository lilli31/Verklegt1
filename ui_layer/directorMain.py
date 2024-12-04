class DirectorMain:

    def __init__(self, id_num, ll_wrapper):
        employee_info = ll_wrapper.getEmployee(id_num)
        self.job_title = employee_info[1]
        self.name = employee_info[0]

    def displayDirectorMain(self, logo):
        print(f"\033[96m{logo}\033[0m")
        print("\n")
        print("-" * 100)
        print("|",(self.name.ljust(33)), (self.job_title.rjust(62)), "|")
        print("-" * 100)
        print("|", "Employees".ljust(13), "|", "Contractors".ljust(13), "|", "Properties".ljust(13), "|", "Work-orders".ljust(13), "|", "My work-orders".ljust(15), "|", "My reports".ljust(14), "|")
        print("-" * 100)
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