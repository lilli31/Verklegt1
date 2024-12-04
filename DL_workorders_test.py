from data_layer.DL_WorkOrder_data import DL_WorkOrders
from models.WorkOrders import WorkOrders

data_layer = DL_WorkOrders()

wo_data = data_layer.FetchWorkOrders()
for workorder in wo_data:
    print(workorder.maintenance_info)



new_workorder = WorkOrders("12", "None", "False", "None", "Blaaaaa", "gera hitt og þetta",
                         "true", "7", "01.01", "now", "false", "false", "closed", "B")

try:
    # Adding a new employee VIRKAR
    result = data_layer.AddWorkOrders(new_workorder)
    print(result) 
    
except Exception as e:
    print("An error occurred during testing:", e)