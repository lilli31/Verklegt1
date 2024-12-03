import csv


class Employee(self):
    
    def __init__(self, employee_id, social_security, info):
        
        """Initializing the employee object with given attributes"""
        
        self.employee_id = employee_id
        self.social_security = social_security
        self.info = info

    def verifyEmployeeID(employeeID):
        
        """Checking if the employee ID is valid"""
        
        if len(employeeID)!= 6:
            return False
        if not employeeID.isdigit():
            return False
        return True
    
    def verifySocialSecurity(self, employee): 

        """Checking if the social security number is valid"""

        if len(employee.social_security)!= 10:
            return False
        if not employee.social_security.isdigit():
            return False
        return True

    def verifyEmployeeInfo(employee.info):
        
        """Checking if the employee information is valid"""
        
        if len(employee.info)< 5 or len(employee.info)> 100:
            return False
        return True
    def verifyEmployeeInfo(employee.info):
        
        """Checking if the employee information is valid"""
        
        if len(employee.info)< 5 or len(employee.info)> 100:
            return False
        return True

    def verifySearchEmployee(employee):
        
        """Checking if the employee is valid"""
        
        if not verifyEmployeeID(employee.employee_id) or not verifySocialSecurity(employee) or not verifyEmployeeInfo(employee.info):
            return False
        return True

    def getEmployeeID(employee_id):
        
        """Returning the employee ID"""
        
        return employee_id

    def getFilteredEmployees(employees):
        
        """Returning a list of filtered employees"""
        
        filtered_employees = []
        for employee in employees:
            if verifySearchEmployee(employee):
                filtered_employees.append(employee)
        return filtered_employees

    def get_all_employees_information(self):

        """Returning all the employee information from the employees.csv file"""

        employees_info = [] #Getting the information from the employees.csv file#
        with open("data_files/employees.csv", newline='') as csvfile: #Reading the data files#
            csvreader = csv.reader(csvfile) #Reading the data from the employees.csv file#
            next(csvreader)  
            for row in csvreader:    
                employees_info.append(Employee(*row)) #Getting the list of employees and their information#     
        return employees_info
            