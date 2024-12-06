
from data_layer.DL_WorkOrder_data import DL_WorkOrders
#from logic_layer.LL_workorder import LL_WorkOrder



class LL_WorkOrder:

    def __init__(self, dl_wrapper):
        self.DL_wrapper = dl_wrapper
        #self.workorders = dl_wrapper.getAllWorkOrder()

    def verifyWorkOrderInfo(self, Work_order_ID: int, Employee: str, Contractor: bool, Contractor_ID: str, Property_IDs: str, Maintenance_info: str, Regular: bool, Days_between_or_when: str, Visible: str, Opens: str, Finished: bool, Approved: bool, State_of_work_order: str, Priority: str):
        try:
            return (
            Work_order_ID and 
            Employee.strip() and 
            Contractor and
            Contractor_ID.strip() and 
            Property_IDs.strip() and 
            Maintenance_info.strip() and
            Regular and 
            Days_between_or_when.strip() and 
            Visible.strip() and 
            Opens.strip() and 
            Finished and 
            Approved and 
            State_of_work_order.strip() and 
            Priority.strip()
        )
        except ValueError:
            return False




"""
from data_layer.DL_WorkOrder_data import DL_WorkOrders
from logic_layer.LL_workorder import LL_WorkOrder

data_layer = DL_WorkOrders()


class LL_WorkOrder:
    def __init__(self, dl_workorder: DL_WorkOrders) -> None:
        self.dl_workorder = dl_workorder

    def verifyNewWorkOrderID(self):
            workorders = self.dl_workorder.FetchWorkOrders()
            highestID = max(workorders)
            # Create a list of missing IDs
            missing_ids = [id for id in range(1, highestID + 1) if id not in workorders]
            # If there are missing IDs, return and append the smallest missing ID
            print(missing_ids)
            if missing_ids:
                smallest_missing_id = min(missing_ids)
                workorders.append(smallest_missing_id)
                #print(f"Smallest missing ID added: {smallest_missing_id}")  # This will print the added ID - þarf þetta í LL?
                print(workorders, smallest_missing_id)
            # If no IDs are missing, append the next ID after the highest ID
            new_id = highestID + 1
            workorders.append(new_id)
            #print(f"New ID added: {new_id}")  # This will print the new ID - þarf þetta í LL?
            print(workorders, new_id)

    verifyNewWorkOrderID()
"""


"""
def verifyNewWorkOrderID(self):
    workorders = [1, 2, 3, 4, 5, 6] 
    highestID = max(workorders)
    # Create a list of missing IDs
    missing_ids = [id for id in range(1, highestID + 1) if id not in workorders]
    # If there are missing IDs, return and append the smallest missing ID
    if missing_ids:
        smallest_missing_id = min(missing_ids)
        workorders.append(smallest_missing_id)
        print(f"Smallest missing ID added: {smallest_missing_id}")  # This will print the added ID - þarf þetta í LL?
        return workorders, smallest_missing_id
    
    # If no IDs are missing, append the next ID after the highest ID
    new_id = highestID + 1
    workorders.append(new_id)
    print(f"New ID added: {new_id}")  # This will print the new ID - þarf þetta í LL?
    return workorders, new_id

# Example of calling the function and updating the list
new_list, new_id = verifyNewWorkOrderID(None)  # passing None for self if it's not in a class
print(new_list)  # Shows the updated workorders list - þarf þetta í LL?
print(new_id)  # Shows the new ID added - þarf þetta í LL?
#ÞETTA VIRKAR EN ÞURFUM EKKI ALLT ÞETTA PRINT DÓT!
"""