from data_layer.DL_employee_data import DL_Employees

data = DL_Employees()

emp_data = data.FetchEmployees()
for employee in emp_data:
    print(employee.email)