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
     
    def UpdateEmployees(self, update_employees: list[Employees]):
        #append
        """Storing all the employees"""

        with open("data_files/employees.csv", 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile)
            writer.writeheader()            
            for employee in update_employees:

                writer.writerow({self.EMPLOYEE_ID: employee.employee_id, 
                                     self.JOB_TITLE: employee.job_title,
                                     self.NAME: employee.name,
                                     self.SSN: employee.ssn,
                                     self.ADDRESS: employee.address,
                                     self.POSTCODE: employee.postcode,
                                     self.HOMEPHONE: employee.homephone,
                                     self.TELEPHONE: employee.telephone,
                                     self.EMAIL: employee.email,
                                     self.DESTINATION_ID: employee.destination_id})
            return update_employees
   
    def AddEmployees(self,employee:Employees):
        
        """Adding a new employee to the employees.csv file"""
        
        with open("data_files/employees.csv", 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([employee.employee_id,
                            employee.job_title,
                            employee.name,
                            employee.ssn,
                            employee.address,
                            employee.postcode,
                            employee.homephone,
                            employee.telephone,
                            employee.email,
                            employee.destination_id])
        return "Employee added successfully"

        
    #Passa að þetta virkar, passa að hann megi sjast tjekka á TA
    def DeleteEmployee(self, employee_id):
        
        """Deleting an employee from the employees.csv file"""
        
        employees_info = self.FetchEmployees() #Getting the list of the employees 
        updated_employees_info = [employee for employee in employees_info if employee.ID!= employee]
        self.Store_employees(updated_employees_info)

        return "Employee deleted successfully"
        
    

    


    
    