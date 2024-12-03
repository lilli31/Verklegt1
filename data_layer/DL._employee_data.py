import csv



class Employee:
    def __init__(self,ID,Job_title,Name,SSN,Address,PostCode,Homephone,Telephone,Email,Place,Place_ID,Country):
        pass

    
    def storeEmployees(self):

        """Storing all the employees information in the employees.csv file"""
        
        with open("data_files/employees.csv", 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(["ID","Job_title","Name","SSN","Address","Postcode","Homephone","Telephone","Email","Place","Place_ID","Country"])
            writer.writerow([self.ID, 
                                 self.Job_title, 
                                 self.Name, 
                                 self.SSN, 
                                 self.Address, 
                                 self.Postcode, 
                                 self.Homephone, 
                                 self.Telephone, 
                                 self.Email, 
                                 self.Place, 
                                 self.Place_ID, 
                                 self.Country])

    def FetchEmployees(self):
        
        """Fetching all the employees information from the employees.csv file"""
        
        employees_info = []
        with open("data_files/employees.csv", 'r') as csvfile:
            reader = csv.reader(csvfile)
            next(reader) # skipping header
            for row in reader:
                employees_info.append(Employee(*row))
        return employees_info
    
    def AddEmployee(employee):
        
        """Adding a new employee to the employees.csv file"""
        
        self.store_employees(employee)
        return "Employee added successfully"
    
    def DeleteEmployee(self.employee):
        
        """Deleting an employee from the employees.csv file"""
        
        employees_info = self.get_all_employees_info()
        updated_employees_info = [employee for employee in employees_info if employee.ID!= employee]
        self.updated_employees(updated_employees_info)
        return "Employee deleted successfully"
    
    def UpdateEmployee(self, employee):
        
        """Updating an employee's information in the employees.csv file"""
        
        employees_info = self.get_all_employees_info()
        updated_employees_info = [employee if employee.ID == employee.ID else employee for employee in employees_info]
        updated_employees_info.append(employee)
        self.updated_employees(updated_employees_info)
        return "Employee updated successfully"
    
   
    
    

    
    