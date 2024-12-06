import csv


from data_layer.DL_contractors_data import DL_Contractor
from data_layer.DL_wrapper import DataLayerWrapper



class LL_Contractor:
    def __init__(self, DL_wrapper):
        self.DL_wrapper = DL_wrapper



    
    def getContractorId(self, contractor_ID):
        all_contractors = DL_Contractor.FetchContractors()
        for contractor in all_contractors:
            if contractor["Contractor_ID"] == contractor_ID:
                return contractor
        return None
    
    #def getContractorId(contractor_ID):
    #    all_contractors = DL_Contractor.FetchContractors()
    #    [contractor['contractorID'] for contractor in all_contractors]

    #    return contractor_ID in all_contractors
    
    

    def verifyContractorID(contractor_ID):
        try:
            all_contractors = DL_Contractor.FetchContractors()
        except Exception as e:
            print(f"Error fetching contractor data: {e}")
            return False
        
        for contractor in all_contractors:
            if contractor["Contractor_ID"] == contractor_ID:
                return True
        return False
        
        #contractor_IDs = [contractor['contractorID'] for contractor in contractor_IDs]
        #return contractorID in contractor_IDs



    def verifyContractorInfo(contractor):
        required = [
            "Contractor_ID", "Name", "Company", "Contact_phone", "Contact_name", "Specialty", "Opening_hours", "Address", "Former_jobs"
        ]
        for variant in required:
            if not getattr(contractor, variant, None):
                return False
        return True



    def verifySearchContractors(contractor_data, Contractor_ID=None, Name=None, Company=None, Contact_phone=None, Contact_name=None, Specialty=None, Opening_hours=None, Address=None, Former_jobs=None):
        contractors_that_match = []
        for contractor in contractor_data:
            if Contractor_ID and contractor['Contractor_ID'] != Contractor_ID:
                continue
            if Name and contractor['Name'] != Name:
                continue
            if Company and contractor['Company'] != Company:
                continue
            if Contact_phone and contractor['Contact_phone'] != Contact_phone:
                continue
            if Contact_name and contractor['Contact_name'] != Contact_name:
                continue
            if Specialty and contractor['Specialty'] != Specialty:
                continue
            if Opening_hours and contractor['Opening_hours'] != Opening_hours:
                continue
            if Address and contractor['Address'] != Address:
                continue
            if Former_jobs and contractor['Former_jobs'] != Former_jobs:
                continue

            contractors_that_match.append(contractor)

        return contractors_that_match



    def getFilteredContractor(contractors: str):
        contractors = DL_Contractor.FetchContractors()
        matched_contractors = [
             contractor for contractor in contractors
             if contractor.lower() in contractor['name'].lower() or
                contractor.lower() in contractor['contractorID'].lower()
         ]
        return matched_contractors



    #þarf ekki að hafa addContractor og updateContractor ??