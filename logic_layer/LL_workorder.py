from data_layer.DL_WorkOrder_data import DL_WorkOrders

class LL_WorkOrder:
    def __init__(self, dl_workorder: DL_WorkOrders) -> None:
        self.dl_workorder = dl_workorder

    def verifyWorkOrderID(self, workorder_ID: int):
        if workorder_ID != int:
            return False
        else:
            return True
        
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
                    

def verifyWorkOrderInfo():
    pass

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