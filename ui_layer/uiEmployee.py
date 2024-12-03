class UI_Employee:

    def displayEmployees():
        pass 

    def displayEmployeeInfo():
        pass

    def search_employee(self, employee_id):

        """Returning the information of employee when given an employee ID"""

        employees_info = self.get_all_employees_info() #Getting all the information about the employee#
        for employee in employees_info: 
            if employee.ID == employee_id: #Check if the employee exists#
                return employee
        return "Employee not found"

    def updateEmployeeInfo():
        pass

    def fillNewEmployeeForm():
        pass