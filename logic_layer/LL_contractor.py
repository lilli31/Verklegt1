import csv
import
from data_layer.DL_wrapper import DataLayerWrapper
from models.Contractors import Contractors



class LL_Contractor:

    def __init__(self, dl_contractor: dl_contractor) -> None:
        self.dl_contractor = dl_contractor
        #nota dependency injection, design patternið

    def getContractorId(self, contractorID):
        return str(contractorID).isdigit()  # Tékka ef það eru bara tölur

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