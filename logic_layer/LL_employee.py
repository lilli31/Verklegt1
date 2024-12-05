from data_layer.DL_employee_data import DL_Employees
from data_layer.DL_wrapper import DataLayerWrapper


class LL_Employee:
    def __init__(self, dl_wrapper):
        self.dl_wrapper = dl_wrapper

    def verifyEmployeeID(employeeID):

        """Checking the if the employee ID is valid"""
        
        employee_ids = DL_Employees.FetchAllEmployees()
        employee_ids = [employee['employeeID'] for employee in employee_ids] #Dict fyrir employee

        return employeeID in employee_ids
    
    #def MatchEmployeesID, hvort að hvert ID sé rétt við hvern employee??
    
    def verifySocialSecurity(self, ssn): 
        
        """Checking if the SSN is valid"""
        
        employee_ssn = DL_Employees.FetchAllEmployees()
        employee_ssn = [employee['SSN'] for employee in employee_ssn] 
        
        
    def verifyEmployeeInfo(employee.info):
        
        """Checking if the employee information is valid"""
        
        #Tjekka hvaða info þarf að tjekka á nákvæmlega
        
    def verifySearchEmployee(employee):
        
        """Checking if the employee is valid"""
        
      #Leita að hverju nákvæmelga, hvað á að vera inn í þessu dallli 
        
   
    # def getEmployeeID(employee_id):
        
    #      """Returning the employee ID"""
        
    #      return employee_id

    # def getFilteredEmployees():
    #      pass

    def getEmployeeInfo(self, ID_num: int) -> tuple:

        # all_employees_info = DataLayerWrapper.getAllEmployees()
        all_info = self.dl_wrapper.getAllEmployees()

        for employee in all_info:
            if int(employee.employee_id) == ID_num:
                name = employee.name
                job_title = employee.job_title
    
        return name, job_title
     


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
            