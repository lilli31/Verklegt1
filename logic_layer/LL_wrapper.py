from logic_layer.LL_employee import LL_Employee
from data_layer.DL_wrapper import DataLayerWrapper

class LogicLayerWrapper:

    def __init__(self):
        self.data_layer_wrapper = DataLayerWrapper()
        self.ll_employee_instance = LL_Employee(self.data_layer_wrapper)

    def getEmployee(self, id_number) -> tuple:
      
        return self.ll_employee_instance.getEmployeeInfo(id_number)
    
    def get_my_work_orders(self, id_number):
        pass
    
    
    