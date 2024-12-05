import unittest
import shutil
from data_layer.DL_employee_data import DL_Employees
from models.Employees import Employees


data_layer = DL_Employees()

emp_data = data_layer.FetchEmployees()
for employee in emp_data:
    print(employee.email)

    #Ef það er til 1 núþegar þá má ekki adda 1 laga;)

new_employee = Employees("20", "Employee", "Yeehaw", "333", "505 Laugavegur", "67890",
                         "+354 555 5555", "+354 555 0000", "jessir@example.com", "5")

try:
    #Adding a new employee VIRKAR
    result = data_layer.AddEmployees(new_employee)
    print(result) 
    
except Exception as e:
    print("An error occurred during testing:", e)

new_employee.employee_id = "11"
new_employee.name = "pippi"

#AddLocation bæta




# try:
    # result = data_layer.UpdateEmployees(new_employee)
    # print([r.name for r in result])
    
# except Exception as e:
#     print("An error occurred during testing:")
#     print(e)

#     print("An error occurred during testing:", e)


result = data_layer.UpdateEmployees(new_employee)
print(result.name, result.address)