import csv
import
from data_layer.DL_wrapper import DataLayerWrapper
from models.Contractors import Contractors



class LL_Contractor:

    def __init__(self, dl_contractor: dl_contractor) -> None:
        self.dl_contractor = dl_contractor
        #nota dependency injection, design patternið

    def __init__(self, dl_wrapper):
        """Initialize the logic layer with a reference to the data layer"""
        """tengja saman"""
        self.dl_wrapper = dl_wrapper

    def getContractorId(self, contractorID):
        if not contractorID.isdigit():  # Tékka ef það eru bara tölur
            return False
        return True

    def verifyContractorID(contractor):
        if len(contractorID)
        return contractor.is_valid_id()

    def verifyContractorInfo(contractor):
        return contractor.is_valid_info()

    def verifySearchContractors(contractor):
        return contractor.is_valid_search()

    def getFilteredContractor(contractor):
        return contractor.get_filtered_contractors()

    def getContractorID(contractor):
        return contractor.get_id()