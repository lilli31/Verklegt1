import sys
import os
import csv
from models.Employees import Employees

class DL_Employees():
    EMPLOYEE_ID = "Employee_ID"
    JOB_TITLE = "Job_title"
    NAME = "Name"
    SSN = "SSN"
    ADDRESS = "Address"
    POSTCODE = "PostCode"
    HOMEPHONE = "Homephone"
    TELEPHONE = "Telephone"
    EMAIL = "Email"
    DESTINATION_ID= "Destination_ID"

    def __init__(self):
        pass
   
    def FetchEmployees(self) -> list[Employees]:

        """Fetching all the employees"""

        all_employees: list[Employees] = []
        with open("data_files/employees.csv", "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                all_employees.append(Employees(row[self.EMPLOYEE_ID], 
                                               row[self.JOB_TITLE],
                                               row[self.NAME],
                                               row[self.SSN],
                                               row[self.ADDRESS],
                                               row[self.POSTCODE],
                                               row[self.HOMEPHONE],
                                               row[self.TELEPHONE],
                                               row[self.EMAIL],
                                               row[self.DESTINATION_ID])) 
        return all_employees
    
    def StoreEmployees(self):
        """Storing the employees information in the employees.csv file"""

        with open("data_files/employees.csv", 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
    #         writer.writerow(["ID","Job_title","Name","SSN","Address","Postcode","Homephone","Telephone","Email","Place","Place_ID","Country"])
    #         writer.writerow([self.ID, 
    #                              self.Job_title, 
    #                              self.Name, 
    #                              self.SSN, 
    #                              self.Address, 
    #                              self.Postcode, 
    #                              self.Homephone, 
    #                              self.Telephone, 
    #                              self.Email, 
    #                              self.Place, 
    #                              self.Place_ID, 
    #                              self.Country])

    # def FetchEmployees(self):
        
    #     """Fetching all the employees information from the employees.csv file"""
        
    #     employees_info = []
    #     with open("data_files/employees.csv", 'r') as csvfile:
    #         reader = csv.reader(csvfile)
    #         next(reader) # skipping header
    #         for row in reader:
    #             employees_info.append(Employee(*row))
    #     return employees_info
    
    # def AddEmployee(employee):
        
    #     """Adding a new employee to the employees.csv file"""
        
    #     self.store_employees(employee)
    #     return "Employee added successfully"
    
    # def DeleteEmployee(self.employee):
        
    #     """Deleting an employee from the employees.csv file"""
        
    #     employees_info = self.get_all_employees_info()
    #     updated_employees_info = [employee for employee in employees_info if employee.ID!= employee]
    #     self.updated_employees(updated_employees_info)
    #     return "Employee deleted successfully"
    
    # def UpdateEmployee(self, employee):
        
    #     """Updating an employee's information in the employees.csv file"""
        
    #     employees_info = self.get_all_employees_info()
    #     updated_employees_info = [employee if employee.ID == employee.ID else employee for employee in employees_info]
    #     updated_employees_info.append(employee)
    #     self.updated_employees(updated_employees_info)
    #     return "Employee updated successfully"
    

    


    
    