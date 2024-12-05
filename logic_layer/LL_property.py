import csv
import LL_property
from data_layer.DL_properties_data import DL_Properties
class LL_Property:

    def __init__(self, dl_wrapper):
        self.dl_wrapper = dl_wrapper

    def VerifyPropertyID(self, propertyID):

        """Checking the if the property ID is valid
           Ná í öll properties í data layerinu og gera error message ef ákveðið id finnst ekki eða er ekki til
           Finna ID í hverju property og tjekka ef id er til fyrir það
           Finna ID hjá hverju property (nota dict)
        """
        try:   
            property_ids = DL_Properties.FetchAllProperties()
        except Exception as e:
            print(f"Error fetching employee data: {e}")
            return False

        property_ids = [employee['employeeID'] for employee in property_ids] 
        return propertyID in property_ids

        # if len(propertyID)== 6 and propertyID == propertyID.capitalize():
        #     letter = propertyID[:3]
        #     digit = propertyID[3:]
        #     if letter.isalpha() and digit.isdigit():
        #         return True   
        # return False

    def getPropertyID(property_id):

        """Returning the employee ID
           Finna id hjá hverjum employee """

        all_properties = DL_Properties.FetchProperties()
        [properties['propertiesID'] for properties in all_properties]

        return property_id in all_properties

    # def getPropertyID(self,property_id):
    #     if not self.verifyPropertyID(id):
    #         return "Not valid ID"
    #     properties = self.dl_property.FetchProperties()
    #     for property in properties:
    #         if property.property_ID == id:
    #             return property
    #     return False 

    def verifyPropertyInfo(self,Destination_ID,Property_ID: str,Property: str,Address: str,Rental_space):
        try:
            return (
            1 <= Destination_ID <= 6 and
            Property_ID.strip() and
            Property.strip() and
            Address.strip() and
            int(Rental_space) > 0
        )
        except ValueError:
            return False

    def SearchProperty(properties_list, **kwargs):

       return [
        property_object for property_object in properties_list
        if all(getattr(property_object, key, None) == value for key, value in kwargs.items())
    ]
    
    def GetFilteredProperties(property): #Hægt að searcha fyrir address og property ID

        properties = DL_Properties.FetchAllPropeties()
        matched_properties = [
            properties for employee in properties
            if employee.lower() in property['address'].lower() or
               employee.lower() in property['propertyID'].lower()
        ]
        return matched_properties
    

    def getPropertyInfo(self, property_id: int) -> tuple:
        all_info = self.dl_wrapper.getAllEmployees()

        for property in all_info:
            if int(property).property_id) == employee_id:
                address = property.name
                property_id = property.job_title
    
        return address, property_id

    def getAllProperties(self, all_properties):
        all_properties = self.DL_property.FetchProperties()
        return all_properties




#       def __init__(self, address, property_ID):
        
           #self.address = address
           #self.property_ID = property_ID
#       sta#ðsetningu, fasteignanúmer,
           #def getFilteredProperties():
           #    wanted = [address] [property_ID]
           #    list(filter(lamda x: x['test']=='abc', listpost))
        


    


    
    


