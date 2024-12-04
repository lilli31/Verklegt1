from data_layer.DL_WorkOrder_data import DL_WorkOrders
from models.WorkOrders import WorkOrders

data_layer = DL_WorkOrders()

wo_data = data_layer.FetchWorkOrders()
for workorder in wo_data:
    print(workorder.work_order_id, workorder.property_ids)