from logic_layer.LL_employee import LL_Employee

class LogicLayerWrapper:

    # def __init__(self):
    #     pass

    @classmethod
    def getEmployee(cls, id_number) -> list:
        ll_employee_instance = LL_Employee()
        return ll_employee_instance.getEmployeeInfo(id_number)