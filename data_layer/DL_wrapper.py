from data_layer.DL_employee_data import DL_Employees

class DataLayerWrapper:

    def __init__(self):
        self.dl_employee_instance = DL_Employees()
    
    def getAllEmployees(self) -> list:
        return self.dl_employee_instance.FetchEmployees()
    
  