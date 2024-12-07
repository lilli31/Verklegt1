from data_layer.DL_WorkOrder_data import DL_WorkOrders

#from data_layer.DL_wrapper import DataLayerWrapper
class LL_WorkOrder:


    def __init__(self, dl_wrapper):
        self.DL_wrapper = dl_wrapper
        #self.workorders = dl_wrapper.getAllWorkOrder()
        self.workorders = dl_wrapper.get_all_work_orders()

    def verifyWorkOrderID(workorderID):

        try:
            workorder_ID = DL_WorkOrders.FetchWorkOrders()
        except Exception as e:
            return False  # Gera error message!!!
        
        workorder_ID = [workorder["Work_Order_ID"] for workorder in workorder_ID]
        return workorderID in workorder_ID
        

    def getWorkOrderID(workorderIDs):
        all_workorders = DL_WorkOrders.FetchWorkOrders()
        [workorder["Work_Order_ID"] for workorder in all_workorders]

        return workorderIDs in all_workorders
    

    
    def getFilteredWorkOrder(workorder: int):
        workorders = DL_WorkOrders.FetchWorkOrders()
        matched_workorders = [
            workorder for workorder in workorders
            if workorder.lower() in workorder["Work_Order_ID"].lower() or
                workorder.lower() in workorder["Employee"].lower() or 
                workorder.lower() in workorder["Property_IDs"].lower()
        ]
        return matched_workorders


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
    """SETJA SVIPAÐA ÚTFÆRSLU Í DATA LAYER (GYLFI)"""
    
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
    

    def getAllWorkOrders(self):
        try:
            # Fetch all work orders from the data layer
            return DL_WorkOrders.FetchWorkOrders()
        except Exception:
            # Return None if fetching fails
            return None

        
    def getWorkOrderInfo(self, workorder_id: int):
        try:
            # Kalla á data layer til að fetcha work order
            work_order = DL_WorkOrders.FetchWorkOrderById(workorder_id)
            
            # Tékka hvort að work order var fundin
            if work_order:
                return work_order  # Skila work order detailum
            else:
                return None
        except Exception:
            return None



    def verifySearchWorkOrders(workorder_data, Work_order_ID = None, Employee = None, Contractor = None, Contractor_ID = None, Property_IDs = None, Maintenance_info = None, Regular = None, Days_between_or_when = None, Visible = None, Opens = None, Finished = None, Approved = None, State_of_work_order = None, Priority = None):
        workorders_that_match = []
        for workorder in workorder_data:
            if Work_order_ID and workorder["Work_order_ID"] != Work_order_ID:
                continue 
            if Employee and workorder["Employee"] != Employee:
                continue 
            if Contractor and workorder["Contractor"] != Contractor:
                continue 
            if Contractor_ID and workorder["Contractor_ID"] != Contractor_ID:
                continue 
            if Property_IDs and workorder["Property_IDs"] != Property_IDs:
                continue 
            if Maintenance_info and workorder["Maintenance_info"] != Maintenance_info:
                continue 
            if Regular and workorder["Regular"] != Regular:
                continue 
            if Days_between_or_when and workorder["Days_between_or_when"] != Days_between_or_when:
                continue 
            if Visible and workorder["Visible"] != Visible:
                continue 
            if Opens and workorder["Opens"] != Opens:
                continue
            if Finished and workorder["Finished"] != Finished:
                continue 
            if Approved and workorder["Approved"] != Approved:
                continue
            if State_of_work_order and workorder["State_of_work_order"] != State_of_work_order:
                continue 
            if Priority and workorder["Priority"] != Priority:
                continue 

            workorders_that_match.append(workorder)

        return workorders_that_match


    def get_my_work_orders(self, id_num) -> list: 
        my_work_orders = []

        for work_order in self.workorders:
            if int(work_order["Work_order_ID"]) == id_num:
                work_order_id = work_order["Work_order_ID"]
                employee = work_order["Employee"]
                contractor = work_order["Contractor"]
                contractor_id = work_order["Contractor_ID"]
                property_ids = work_order["Property_IDs"]
                maintenance_info = work_order["Maintenance_info"]
                regular = work_order["Regular"]
                days_between_or_when = work_order["Days_between_or_when"]
                visible = work_order["Visible"]
                opens = work_order["Opens"]
                finished = work_order["Finished"]
                approved = work_order["Approved"]
                state_of_work_order = work_order["State_of_work_order"]
                priority = work_order["Priority"]

                if contractor == "True":
                    contractors = self.dl_wrapper.get_all_contractors()
                    for contractor_object in contractors:
                        if contractor_object.contractor_id == contractor_id:
                            contractor_name = contractor_object.name
                            contractor_phone = contractor_object.contant_phone 
                            contractor_specialty = contractor_object.specialty

                            my_work_orders.append([
                                work_order_id, employee, contractor_name, contractor_phone, 
                                contractor_specialty, maintenance_info, regular, 
                                days_between_or_when, visible, opens, finished, approved, 
                                state_of_work_order, priority
                            ])
                            break
                else: 
                    my_work_orders.append([
                        work_order_id, employee, None, None, None, maintenance_info, 
                        regular, days_between_or_when, visible, opens, finished, approved, 
                        state_of_work_order, priority
                    ])
                    
        return my_work_orders


