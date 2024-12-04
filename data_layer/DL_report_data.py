import csv
from models.Report import Reports

class DL_Report(Reports):
    def __init__(self):
         super().__init__()

    #def store_reports(self):
        

    def fetch_reports(self):
        with open("reports.csv", "r") as file:
            reader = csv.reader(file)
            lines = list(reader)
            
            keys = lines[0]
            reports_dict = {key: [] for key in keys}
            for row in lines[1:]:
                for key, value in zip(keys, row):
                    reports_dict[key].append(value)
        return reports_dict


    def add_reports(self):
        pass

    def delete_reports(self):
        pass

    def update_reports(self):
        pass

 