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
        for id in range(0, highestID+1):
            if id <= highestID or id == 0:
                for newid in range(0, highestID+1):
                    if newid == id:
                        continue
                    

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


    def get_my_work_orders():
        pass