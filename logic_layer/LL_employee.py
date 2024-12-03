class LL_Employee:

    # def verifyEmployeeID(employeeID):
        
    #     """Checking if the employee ID is valid"""
        
    #     if len(employeeID)!= 6:
    #         return False
    #     if not employeeID.isdigit():
    #         return False
    #     return True
    
    # def verifySocialSecurity(self, employee): 

    #     """Checking if the social security number is valid"""

    #     if len(employee.social_security)!= 10:
    #         return False
    #     if not employee.social_security.isdigit():
    #         return False
    #     return True

    # def verifyEmployeeInfo(employee.info):
        
    #     """Checking if the employee information is valid"""
        
    #     if len(employee.info)< 5 or len(employee.info)> 100:
    #         return False
    #     return True

    # def verifySearchEmployee(employee):
        
    #     """Checking if the employee is valid"""
        
    #     if not verifyEmployeeID(employee.employee_id) or not verifySocialSecurity(employee) or not verifyEmployeeInfo(employee.info):
    #         return False
    #     return True

    # def getEmployeeID(employee_id):
        
    #     """Returning the employee ID"""
        
    #     return employee_id

    # def getFilteredEmployees():
    #     pass

    def getEmployeeInfo(self, ID_num) -> list:

        all_employees_info = dict
        name_and_job_list = []

        for id_number in all_employees_info:
            if id_number == ID_num:
                name = id_number[1]
                job = id_number[0]
                name_and_job_list.append(name)
                name_and_job_list.append(job)

        return name_and_job_list


        # self.ID_num = ID_num #Fyrir test
        # Employee = "Employee" #Fyrir test
        # Name = "The Best Employee" #Fyrir test


        # return [Employee, Name] #Fyrir test

        # """Returning all the employee information from the employees.csv file"""

        # employees_info = [] #Getting the information from the employees.csv file#
        # with open("data_files/employees.csv", newline='') as csvfile: #Reading the data files#
        #     csvreader = csv.reader(csvfile) #Reading the data from the employees.csv file#
        #     next(csvreader)  
        #     for row in csvreader:    
        #         employees_info.append(Employee(*row)) #Getting the list of employees and their information#     
        # return employees_info
            