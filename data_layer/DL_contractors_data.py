import csv
from models.Contractors import Contractors

class DL_Contractor():

    CONTRACTOR_ID = "Contractor_ID"
    NAME = "Name"
    COMPANY = "Company"
    CONTACT_PHONE = "Contact_phone"
    CONTACT_NAME = "Contact_name"
    SPECIALTY = "Specialty"
    OPENING = "Opening_hours"
    ADDRESS = "Address"
    JOBS = "Former_jobs"

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
                                                   row[self.CONTACT_PHONE],
                                                   row[self.CONTACT_NAME], 
                                                   row[self.SPECIALTY],
                                                   row[self.OPENING],
                                                   row[self.ADDRESS],
                                                   row[self.JOBS]))
                
        return all_contractors


    def UpdateContractors(self, UpdateContractors: list[Contractors]):
        """Update all the contractors"""

        contractors=self.FetchContractors()
        with open("data_files/contractors.csv", 'w', newline='', encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, [self.CONTRACTOR_ID,self.NAME,self.COMPANY,self.CONTACT_PHONE,self.CONTACT_NAME,self.SPECIALTY,self.OPENING,self.ADDRESS,self.JOBS])
            writer.writeheader()

            for contractor in UpdateContractors:
                try: 
                    i = contractors.index(contractor)
                    contractors[i] = contractor
                except:
                    pass
                
            for contractor in contractors:

                writer.writerow({self.CONTRACTOR_ID: contractor.contractor_id, 
                                 self.NAME: contractor.name,
                                 self.COMPANY: contractor.company,
                                 self.CONTACT_NAME: contractor.contact_name,
                                 self.CONTACT_PHONE: contractor.contact_phone,
                                 self.ADDRESS: contractor.address,
                                 self.SPECIALTY: contractor.specialty,
                                 self.OPENING: contractor.opening_hours,
                                 self.JOBS: contractor.former_jobs})
            return UpdateContractors
        


    def AddContractors(self,contractors: Contractors):
        
        """Adding a new contractor to the contractors.csv file"""
        
        with open("data_files/contractors.csv", 'a', newline='', encoding="utf-8") as csvfile:
            for line in contractors.csv:
                """ID númer stimpla"""
                writer = csv.writer(csvfile)
                writer.writerow([contractors.contractor_id,
                                contractors.name,
                                contractors.contact_name,
                                contractors.contact_phone,
                                contractors.address,
                                contractors.opening_hours,
                                contractors.former_jobs])
            return "Contractor added successfully"
        

        
    def FindContractorByKeyword(self, keyword: str) -> Contractors:
        found_contractors = []
        with open("data_files/contractors.csv", 'r') as csvfile:
            reader = csv.reader(csvfile, delimiter='\n')
            for line in reader:
                if keyword.lower() in line[0].lower():
                    found_contractors.append(line)
        return found_contractors

            