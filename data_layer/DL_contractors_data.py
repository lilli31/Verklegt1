import csv
import sys
import os
from models.Contractors import Contractors

class DL_Contractor():
    CONTRACTOR_ID = "Contractor_id"
    NAME = "Name"
    COMPANY = "Company"
    PHONE = "Phone"
    CONTACT_NAME = "Contact name"
    OPENING = "Opening"
    ADDRESS = "Address"
    JOBS = "Jobs"

    def __init__(self):
        pass

    def FetchContractors(self) -> list[Contractors]:

        """Fetching all contractors"""

        all_contractors: list[Contractors] = []
        with open("data_files/Contractors.csv", "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                all_contractors.append(Contractors(row[self.CONTRACTOR_ID], 
                                                   row[self.NAME],
                                                   row[self.COMPANY],
                                                   row[self.PHONE],
                                                   row[self.CONTACT_NAME], 
                                                   row[self.OPENING],
                                                   row[self.ADDRESS],
                                                   row[self.JOBS]))
                
        return all_contractors


    def GetAllContractors(self):
        """Returning all the contractor information from the contractors.csv file."""
        contractors = []  #Getting the information from the contractors.csv file
        with open("models/Contractors.py", newline='') as csv_file:
            csvreader = csv.reader(csv_file) #Reading the data from the contractors.csv file
            next(csvreader)  #Skip the header row
            for line in csvreader:
                contractors.append(Contractors(line))  #Getting the list of contractors and their information
            for line in csvreader:
                del line['']
        return contractors

    def UpdateContractors():
        
    def AddEmployees(self,contractors: Contractors):
        
        """Adding a new contractor to the employees.csv file"""
        
        with open("data_files/employees.csv", 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([contractors.contractor_id,
                             contractors.name,
                             contractors.contact_name,
                             contractors.address,
                             contractors.opening,
                             contractors.jobs])
                             
        return "Contractor added successfully"