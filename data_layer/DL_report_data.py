import csv
from models.Report import Reports


class DL_Report(Reports):
    REPORT_ID = "Report_ID"
    WORK_ORDER_ID = "Work order ID"
    WORK_DONE = "Work done"
    CONTRACTOR =  "Contractor"
    CONTRACTOR_ID = "Contractor ID"
    ADDITIONAL_REPORT_INFO = "Additional report info"
    MATERIAL_COST = "Material cost"
    CONTRACTOR_COST = "Contractor cost"
    TOTAL_COST = "Total cost"

    def __init__ (self):
        pass
        


    def FetchReports(self) -> list[Reports]: 

        """Fetching all the reports"""

        all_reports: list[Reports] = []
        with open("data_files/reports.csv", "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                all_reports.append(Reports(row[self.REPORT_ID], 
                                               row[self.WORK_ORDER_ID],
                                               row[self.WORK_DONE],
                                               row[self.CONTRACTOR],
                                               row[self.CONTRACTOR_ID],
                                               row[self.ADDITIONAL_REPORT_INFO],
                                               row[self.MATERIAL_COST],
                                               row[self.CONTRACTOR_COST],
                                               row[self.TOTAL_COST])) 
        return all_reports



    def AddReport(self,report:Reports):
        
        """Adding a new report to the reports.csv file"""
        
        with open("data_files/reports.csv", 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([report.report_ID,
                            report.work_order_ID,
                            report.work_done,
                            report.contractor,
                            report.contractor_ID,
                            report.additional_report_info,
                            report.material_cost,
                            report.contractor_cost,
                            report.total_cost])
        return "Report added successfully"

    def DeleteReports(self):
        pass


    def UpdateReports(self):
        pass

    def MarkReportAsDone(self):



 