import csv

class Employee:
    def __init__(self,ID,Job_title,Name,SSN,Address,PostCode,Homephone,Telephone,Email,Place,Place_ID,Country):
        pass

    def get_employees_by_job_title(self, job_title):
        
        """Returning the employees with a job title inot the employees.csv file"""

        employees_info = self.get_all_employees_info()
        employees_with_job_title = [employee for employee in employees_info if employee.Job_title == job_title]
        return employees_with_job_title
            
    def get_all_employees_info(self):

        """Returning all the employee information from the employees.csv file"""

        employees_info = []
        with open("data_files/employees.csv", newline='') as csvfile:
            csvreader = csv.reader(csvfile)
            next(csvreader)  
            for row in csvreader:
                employees_info.append(Employee(*row))
        return employees_info
    
    def search_employee(self, employee_id):

        """Returning the information of employee when given an employee ID"""

        employees_info = self.get_all_employees_info()
        for employee in employees_info:
            if employee.ID == employee_id:
                return employee
        return "Employee not found"
    
    def update_employee_info(self, employee_id, updated_information):  

        """Updating an employee's information in the employees.csv file"""

        employees_info = self.get_all_employees_info()
        for employee in employees_info:
            if employee.ID == employee_id:
                employee.update(updated_information)
                self.update_employees_to_file(employees_info)
                return "Employee information updated successfully"
        return "Employee not found"
    
    def updated_employees(self, employees_info):

        """Writing the updated employee information back to the employees.csv file"""

        with open("data_files/employees.csv", "w", newline='') as csvfile:
            fieldnames = ["ID", "Job_title", "Name", "SSN", "Address", "Post_code", "Homephone", "Telephone", "Email", "Place", "Place_ID", "Country"]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for employee in employees_info:
                writer.writerow(employee)
    
    def delete_employee(self, employee_id):

        """Delete an employee from the employees.csv file"""

        employees_info = self.get_all_employees_info()
        updated_employees_info = [employee for employee in employees_info if employee.ID != employee_id]
        self.write_employees_to_file(updated_employees_info)
        return "Employee deleted successfully"
    
    def create_new_employee(self, new_employee):

        """Create a new employee in the employees.csv file"""

        employees_info = self.get_all_employees_info()
        employees_info.append(new_employee)
        self.write_employees_to_file(employees_info)
        return "New employee added successfully"
    
    def get_employees_by_location(self, location):

        """Returning all employees from a different location in the employees.csv file"""

        employees_info = self.get_all_employees_info()
        employees_in_location = [employee for employee in employees_info if employee.Place == location]
        return employees_in_location
    
    def get_employees_by_country(self, country):

        """Returning all employees from a different specific country in the employees.csv file"""

        employees_info = self.get_all_employees_info()
        employees_in_country = [employee for employee in employees_info if employee.Country == country]
        return employees_in_country
    
  
    

    
    