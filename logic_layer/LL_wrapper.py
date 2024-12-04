from logic_layer.LL_employee import LL_Employee

class LogicLayerWrapper:

    def __init__(self):
        self.ll_employee_instance = LL_Employee()

    def getEmployee(self, id_number) -> list:
      
        return self.ll_employee_instance.getEmployeeInfo(id_number)