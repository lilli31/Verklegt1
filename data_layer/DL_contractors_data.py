import csv

class Contractor():

    def get_all_contractors_id(self):
        """Returning all the contractor information from the contractors.csv file."""
        contractors = []  #Getting the information from the contractors.csv file
        with open("models/Contractors.py", newline='') as csv_file:
            csvreader = csv.reader(csv_file) #Reading the data from the contractors.csv file
            next(csvreader)  #Skip the header row
            for line in csvreader:
                contractors.append(Contractor(line))  #Getting the list of contractors and their information
            for line in csvreader:
                del line['']
        return contractors

    def update_contractors_info():  #update contactors information
        contractors = []
        with open("models/Contractors.py") as info:
            info_data = csv.reader(info)
            for row in info_data:
                contractors.append(row)
            return contractors
        
        


        
