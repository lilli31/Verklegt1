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


    #   def makeNewPropertyID(self, Destination_ID: int, Property_ID: str, Property: str, Address: str, Rental_space: int):
    #   þetta fer í ui layer held ég


    def getPropertyID(self,id: str):
        if not self.verifyPropertyID(id):
            return "Not valid ID"
        properties = self.dl_property.FetchProperties()
        for property in properties:
            if property.property_ID == id:
                return property
        return False #búa til error?


    def verifyPropertyInfo(self,Destination_ID,Property_ID: str,Property: str,Address: str,Rental_space):
        if not (1 <= Destination_ID <= 6):
            return False
        if not Property_ID.strip():
            return False
        if not Property.strip():
            return False
        if not Address.strip():
            return False
        try:
            Rental_space = int(Rental_space):
        except ValueError:
            return False
        return True


    def searchProperty(properties_data, Destination_ID=None, Property_ID=None, Property=None, Address=None):
        properties_that_match = []

        #Fara yfir hverja property í datanu
        for property in properties_data:

            if Destination_ID and property['Destination_ID'] != Destination_ID:
                continue
            if Property_ID and property['Property_ID'] != Property_ID:
                continue
            if Property and property['Property'] != Property:
                continue
            if Address and property['Address'] != Address:
                continue

            #Ef allt passar er hægt að bæta við
            properties_that_match.append(property)

        return properties_that_match

#       def __init__(self, address, property_ID):
        
           #self.address = address
           #self.property_ID = property_ID
#       sta#ðsetningu, fasteignanúmer,
           #def getFilteredProperties():
           #    wanted = [address] [property_ID]
           #    list(filter(lamda x: x['test']=='abc', listpost))
        


    def getAllProperties(self):
        return self.dl_property.FetchProperties()


    def addNewProperty(self, Destination_ID, Property_ID, Property, Address, Rental_space):
        if not self.verifyPropertyInfo(Destination_ID, Property_ID, Property, Address, Rental_space):
            return "Invalid information"
        new_property = {"Destination_ID": Destination_ID, "Property_ID": Property_ID, "Property": Property, "Address": Address, "Rental_space": Rental_space}
        return "Property added"
    


