import csv
import LL_property
from data_layer.DL_properties_data import DL_Properties
class LL_Property:

    def __init__(self, dl_property: DL_Properties) -> None:
        self.dl_property = dl_property
        #nota dependency injection, design patternið

    def verifyPropertyID(self, propertyID: str):
        if len(propertyID)== 6 and propertyID == propertyID.capitalize():
            letter = propertyID[:3]
            digit = propertyID[3:]
            if letter.isalpha() and digit.isdigit():
                return True   
        return False
    
    def getPropertyByID(self,id: str):
        if not self.verifyPropertyID(id):
            return "Not valid ID"
        properties = self.dl_property.FetchProperties()
        for property in properties:
            if property.property_ID == id:
                return property
        return False #búa til error?

    def verifyPropertyInfo(self,Destination_ID,Property_ID,Property,Address,Rental_space):
        if 1 <= Destination_ID <= 6:
            if Property_ID =: #verifyPropertyID()
                if Address == bool(Address.strip()):
                    if Rental_space


        pass

    def verifySearchProperty():
        pass

    def getFilteredProperties():
        pass

    def getPropertyID():
        pass

    def getAllProperties(self):
        return self.dl_property.FetchProperties()
    
dl = DL_Properties()
a = LL_Property(dl)

