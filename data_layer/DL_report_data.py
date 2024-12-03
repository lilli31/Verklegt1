import csv
from models.Report import Reports

class DL_Report(Reports):
    def __init__(self):
         super().__init__()

    def store_reports(self):
        pass

    def fetch_reports(self):
        file = open("reports.csv", "r")
        reader = csv.reader(file)
        rows = list(reader)

        keys = rows[0]

        reports_dict = {key: [] for key in keys}

        for row in rows[1:]:
                for key, value in zip(keys, row):
                    reports_dict[key].append(value)
        return reports_dict


    def add_reports(self):
        pass

    def delete_reports(self):
        pass

    def update_reports(self):
        pass

 