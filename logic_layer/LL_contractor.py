import csv



class Contractor(self):
    def __init__(self, id, name, phone, email, address):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address 

    def getContractorId(self):
        return self.id

    def verifyContractorID(contractor):
        return contractor.is_valid_id()

    def verifyContractorInfo(contractor):
        return contractor.is_valid_info()

    def verifySearchContractors(contractor):
        return contractor.is_valid_search()

    def getFilteredContractor(contractor):
        return contractor.get_filtered_contractors()

    def getContractorID(contractor):
        return contractor.get_id()