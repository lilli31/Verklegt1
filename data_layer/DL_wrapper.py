from data_layer.DL_employee_data import DL_Employees

class DataLayerWrapper:
    
    @classmethod
    def getAllEmployees(cls) -> list:
        dl_employee_instance = DL_Employees()
        return dl_employee_instance.FetchEmployees()