from data_layer.DL_WorkOrder_data import DL_WorkOrders
from models.WorkOrders import WorkOrders

data_layer = DL_WorkOrders()

wo_data = data_layer.FetchWorkOrders()
for workorder in wo_data:
    print(workorder.maintenance_info)



new_workorder = WorkOrders("99", "None", "False", "None", "Blaaaaa", "gera hitt og þetta",
                         "true", "7", "01.01", "now", "false", "false", "closed", "B")

try:
    # Adding a new employee VIRKAR
    result = data_layer.AddWorkOrder(new_workorder)
    print(result) 
    
except Exception as e:
    print("An error occurred during testing:")
    print(e)


new_workorder.work_order_id = "6"
new_workorder.contractor = "ja"

try:
    # Adding a new employee EKKI VIRKAR
    result = data_layer.UpdateWorkOrder(new_workorder)
    print(result)
    #print([r.contractor for r in result]) 
    
except Exception as e:
    print("An error occurred during testing:", e)