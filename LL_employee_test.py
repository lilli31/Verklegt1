from DL_employee_data import DL_Employees  
from LL_employee import LL_Employees
from models.Employees import Employees

data_layer = DL_Employees()

#Setja inn employee ID 
test_id = "12"

if LL_Employees (test_id, data_layer):
    print(f"Employee ID {test_id} is valid.")
else:
    print(f"Employee ID {test_id} is not valid.")