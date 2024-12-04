from data_layer.DL_report_data import DL_Report
from models.Report import Reports


data_layer = DL_Report()

rep_data = data_layer.FetchReports()
for reports in rep_data:
    print(reports.contractor)


new_report = Reports("", "", "", "", "", "", "", "", "")

try:
    result = data_layer.AddReport(new_report)
    print(result) 
    
except Exception as e:
    print("An error occurred during testing:")

new_report.work_order_ID = "19"
new_report.work_done = "kiki"


try:
    result = data_layer.UpdateReports(new_report)
    print([r.name for r in result]) 
    
except Exception as e:
    print("An error occurred during testing:")
    print(e)

    print("An error occurred during testing:", e)