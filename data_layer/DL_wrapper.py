from data_layer.DL_employee_data import DL_Employees
from data_layer.DL_WorkOrder_data import DL_WorkOrders
from data_layer.DL_report_data import DL_Report
from data_layer.DL_contractors_data import DL_Contractor

class DataLayerWrapper:

    def __init__(self):
        self.dl_employee_instance = DL_Employees()
        self.dl_work_orders = DL_WorkOrders()
        self.dl_reports = DL_Report()
        self.dl_contractors = DL_Contractor()
    
    def getAllEmployees(self) -> list:

        return self.dl_employee_instance.FetchEmployees()
    
    def get_all_work_orders(self) -> list:

        return self.dl_work_orders.FetchWorkOrders()
  
    def get_all_reports(self) -> list:

        return self.dl_reports.FetchReports()
    
    def get_all_contractors(self) -> list:

        return self.dl_contractors.FetchContractors()