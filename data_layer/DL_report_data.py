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
                all_properties.append(Properties(row[self.DEESTINATION_ID], 
                                               row[self.PROPERTY_ID],
                                               row[self.PROPERTY],
                                               row[self.ADDRESS],
                                               row[self.RENTAL_SPACE],)) 
        return all_properties

    def add_reports(self):
        pass


    def delete_reports(self):
        pass


    def update_reports(self):
        pass

 