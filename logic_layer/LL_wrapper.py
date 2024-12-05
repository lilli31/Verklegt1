from logic_layer.LL_employee import LL_Employee
from data_layer.DL_wrapper import DataLayerWrapper
from logic_layer.LL_workorder import LL_WorkOrder
from logic_layer.LL_report import LL_Report

class LogicLayerWrapper:

    def __init__(self):
        self.data_layer_wrapper = DataLayerWrapper()
        self.ll_employee_instance = LL_Employee(self.data_layer_wrapper)
        self.ll_work_order = LL_WorkOrder(self.data_layer_wrapper)
        self.ll_reports = LL_Report(self.data_layer_wrapper)

    def getEmployee(self, id_number) -> tuple:
      
        return self.ll_employee_instance.getEmployeeInfo(id_number)
    
    def get_work_orders(self, id_number):
        
        return self.ll_work_order.get_my_work_orders(id_number)
    
    def get_reports(self, id_number) -> list:

        return self.ll_reports.get_my_reports(id_number)
    
    def sort_reports(self, reports: list) -> list:

        return self.ll_reports.sort_my_reports(reports)