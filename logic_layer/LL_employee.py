from data_layer.DL_employee_data import DL_Employees
from data_layer.DL_wrapper import DataLayerWrapper


class LL_Employee:
    def __init__(self, dl_wrapper):
        self.dl_wrapper = dl_wrapper

    def verifyEmployeeID(employeeID): 

        """Checking the if the employee ID is valid
           Ná í alla employees í data layerinu og gera error message ef ákveðið id finnst ekki eða er ekki til
           Finna ID hjá hverjum employee og tjekka ef id er til
           Finna ID hjá hverjum employee (nota dict)
        """
        try:   
            employee_ids = DL_Employees.FetchAllEmployees()
        except Exception as e:
            print(f"Error fetching employee data: {e}")
            return False

        employee_ids = [employee['employeeID'] for employee in employee_ids] 
        return employeeID in employee_ids
    
    def getEmployeeID(employee_id):
        
        """Returning the employee ID
           Finna id hjá hverjum employee """

        all_employees = DL_Employees.fetchAllEmployees()
        [employee['employeeID'] for employee in all_employees]

        return employee_id in all_employees
        
    def verifySocialSecurity(self, ssns): 
        
        """Checking if the SSN is valid
           Finna kennitölu hjá hverjum employee og tjekka ef það er til"""
        
        employee_ssn = DL_Employees.FetchAllEmployees()
        employee_ssn = [employee['SSN'] for employee in employee_ssn] 
        
        return ssns in employee_ssn

    def GetDestinationByID(self) -> list[DL_Employees]:

        """Returning the destination of the employee
           Finna staðsetningu hvers employee by id-inu hans"""
        
        all_employees = DL_Employees.fetchAllEmployees()
        return [employee['destination_id'] for employee in all_employees]
        
    def verifySearchEmployee(employee): #Er að gera þannig allir geta searchað af employee
        
        """Verify that it is possible to search for employees
           Náum í alla employees, fyrir alla employees þá erum við að ná í frá csv nöfnin á employees"""

        employees = DL_Employees.FetchAllEmployees()
        matched_employees = [
            employee for employee in employees
            if employee.lower() in employee['name'].lower() or
               employee.lower() in employee['employeeID'].lower()
        ]
        return matched_employees

    #def GetFilteredEmployeesByID(self) -> List[DL_Employees]:
        pass

    def getEmployeeInfo(self, employee_id: int) -> tuple:
        all_info = self.dl_wrapper.getAllEmployees()

        for employee in all_info:
            if int(employee.employee_id) == employee_id:
                name = employee.name
                job_title = employee.job_title
    
        return name, job_title

        
    #def verifyEmployeeInfo(employee.info):
        #pass
   

    #def getEmployeeInfo(self):
        Get_all_employees_info = DataLayerWrapper.getAllEmployees()
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
            