import csv




class Employee:
    def __init__(self,ID,Job_title,Name,SSN,Address,PostCode,Homephone,Telephone,Email,Place,Place_ID,Country):
        pass

    def get_employees_by_job_title(self, job_title):

        """Returning all the employees with a job title from the employees.csv file"""

        employees_info = self.get_all_employees_info() #Getting all the information about the employees"""
        employees_with_job_title = [employee for employee in employees_info if employee.Job_title == job_title] 
        return employees_with_job_title #For each employee with a job title we are returning the information"""

    def get_all_employees_info(self):

        """Returning all the employee information from the employees.csv file"""

        employees_info = [] #Getting the information from the employees.csv file#
        with open("data_files/employees.csv", newline='') as csvfile: #Reading the data files#
            csvreader = csv.reader(csvfile) #Reading the data from the employees.csv file#
            next(csvreader)  
            for row in csvreader:    
                employees_info.append(Employee(*row)) #Getting the list of employees and their information#     
        return employees_info
    
    def search_employee(self, employee_id):

        """Returning the information of employee when given an employee ID"""

        employees_info = self.get_all_employees_info() #Getting all the information about the employee#
        for employee in employees_info: 
            if employee.ID == employee_id: #Check if the employee exists#
                return employee
        return "Employee not found"
    
    def update_employee_info(self, employee_id, updated_information):  

        """Updating an employee's information in the employees.csv file"""

        employees_info = self.get_all_employees_info()
        for employee in employees_info:
            if employee.ID == employee_id: #Getting an employee id  and make it match the employee#
                employee.update(updated_information) # the information is updated#
                self.update_employees_to_file(employees_info)
                return "Employee information updated successfully"
        return "Employee not found"
    
    def updated_employees(self, employees_info):

        """Writing the updated employee information back to the employees.csv file"""
        
        with open("data_files/employees.csv", 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID","Job_title","Name","SSN","Address","Postcode","Homephone","Telephone","Email","Place","Place_ID","Country"])
            for employee in employees_info:
                writer.writerow([employee.ID, 
                                 employee.Job_title, 
                                 employee.Name, 
                                 employee.SSN, 
                                 employee.Address, 
                                 employee.Postcode, 
                                 employee.Homephone, 
                                 employee.Telephone, 
                                 employee.Email, 
                                 employee.Place, 
                                 employee.Place_ID, 
                                 employee.Country])

    
    def delete_employee(self, employee_id):

        """Delete an employee from the employees.csv file"""

        employees_info = self.get_all_employees_info() # get all the employees information from the employees file#
        updated_employees_info = [employee for employee in employees_info if employee.ID != employee_id]
        self.update_employee_info(updated_employees_info) # write the employees information to the file to be deleted from the data filie#
        return "Employee deleted successfully"
    
    def create_new_employee(self, new_employee):

        """Create a new employee in the employees.csv file"""

        employees_info = self.get_all_employees_info()
        employees_info.append(new_employee) #Adding a new employee#
        self.update_employee_info(employees_info) 
        return "New employee added successfully"
    
    def get_employees_by_destiantion(self, destination):

        """Returning all employees from a different destinations in the destinations.csv file"""

        destinations_info = self.get_all_destinations_info()
        employees_destination = [employee for employee in destinations_info if employee.destination == destination]
        return employees_destination
    
    def get_employees_by_place(self, place):
        
        """Returning all employees from a different specific place in the employees.csv file"""
        
        employees_info = self.get_all_employees_info()
        employees_in_place = [employee for employee in employees_info if employee.place == place] 
        return employees_in_place

    def get_employees_by_country(self, country):

        """Returning all employees from a different specific country in the employees.csv file"""

        employees_info = self.get_all_employees_info() #Getting all the information about the employees#
        employees_in_country = [employee for employee in employees_info if employee.Country == country] #getting all the information about the employees in the country#
    
  
    

    
    