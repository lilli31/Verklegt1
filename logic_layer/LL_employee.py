class LL_Employee:

    def verifyEmployeeID():
        pass

    def verifySocialSecurity():
        pass

    def verifyEmployeeInfo():
        pass

    def verifySearchEmployee():
        pass

    def getEmployeeID():
        pass

    def getFilteredEmployees():
        pass

    def getEmployeeInfo(self, ID_num):

        self.ID_num = ID_num #Fyrir test
        Employee = "Employee" #Fyrir test
        Name = "The Best Employee" #Fyrir test


        return [Employee, Name] #Fyrir test

        """Returning all the employee information from the employees.csv file"""

        # employees_info = [] #Getting the information from the employees.csv file#
        # with open("data_files/employees.csv", newline='') as csvfile: #Reading the data files#
        #     csvreader = csv.reader(csvfile) #Reading the data from the employees.csv file#
        #     next(csvreader)  
        #     for row in csvreader:    
        #         employees_info.append(Employee(*row)) #Getting the list of employees and their information#     
        # return employees_info