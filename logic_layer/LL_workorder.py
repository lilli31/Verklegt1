from data_layer.DL_WorkOrder_data import DL_WorkOrders
from data_layer.DL_wrapper import DataLayerWrapper

class LL_WorkOrder:
    def __init__(self, dl_wrapper):
        self.dl_wrapper = dl_wrapper

    def verifyWorkOrderID(workorderID):

        try:
            workorder_ID = DL_WorkOrders.FetchWorkOrders()
        except Exception as e:
            return False  # Gera error message!!!
        
        workorder_ID = [workorder["workorderID"] for workorder in workorder_ID]
        return workorderID in workorder_ID
        

    """    
    def verifyNewWorkOrderID(self):
        workorders = self.dl_workorder.FetchWorkOrders()
        highestID = max(workorders)
        # Create a list of missing IDs
        missing_ids = [id for id in range(1, highestID + 1) if id not in workorders]
        # If there are missing IDs, return and append the smallest missing ID
        if missing_ids:
            smallest_missing_id = min(missing_ids)
            workorders.append(smallest_missing_id)
            #print(f"Smallest missing ID added: {smallest_missing_id}")  # This will print the added ID - þarf þetta í LL?
            return workorders, smallest_missing_id
        
        # If no IDs are missing, append the next ID after the highest ID
        new_id = highestID + 1
        workorders.append(new_id)
        #print(f"New ID added: {new_id}")  # This will print the new ID - þarf þetta í LL?
        return workorders, new_id
    """             

def verifyWorkOrderInfo(self, Work_order_ID, Employee, Contractor, Contractor_ID, Property_IDs, Maintenance_info, Regular, Days_between_or_when, Visible, Opens, Finished, Approved, State_of_work_order, Priority):
    if not isinstance(Work_order_ID, int):
        return False
    if not isinstance(Employee.strip(), str):
        return False
    if not isinstance(Contractor, bool):
        return False
    if not isinstance(Contractor_ID.strip(), str):
        return False
    if not isinstance(Property_IDs, str) or len(Property_IDs) != 6:
        return False
    if not isinstance(Maintenance_info.strip(), str):
        return False
    if not isinstance(Regular, bool):
        return False
    if not isinstance(Days_between_or_when.strip(), str):
        return False
    if not isinstance(Visible.strip(), str):
        return False
    if not isinstance(Opens.strip(), str):
        return False
    if not isinstance(Finished, bool):
        return False
    if not isinstance(Approved, bool):
        return False
    if isinstance(State_of_work_order, str) or State_of_work_order.strip() not in ("Closed", "Open"):
        return False
    if isinstance(Priority, str) or Priority.strip() not in ("A", "B", "C"):
        return False
    return True

def verifySearchWorkOrders():
    pass

def getFilteredWorkOrder(filter: str):
    pass

def getAllWorkOrder():
    pass

def getWorkOrderID():
    pass


def get_my_work_orders(self, id_num):
    pass

