import csv
import LL_property
from data_layer.DL_properties_data import DL_Properties
class LL_Property:

    def __init__(self, dl_property: DL_Properties) -> None:
        self.dl_property = dl_property
        #nota dependency injection, design patternið

    def verifyPropertyID(self, propertyID: str):
        if len(propertyID)!= 5:
             return False
        if propertyID != propertyID.capitalize():
             return False
        return True #og meira
    
    def getPropertyByID(self,id: str):
        if not self.verifyPropertyID(id):
            return "Not valid ID"
        properties = self.dl_property.FetchProperties()
        for property in properties:
            if property.property_ID == id:
                return property
        return False #búa til error?

    def verifyPropertyInfo():
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

