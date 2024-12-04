import csv
import os
from models.properties import Properties


class DL_Properties():
    DEESTINATION_ID = "Destination_ID"
    PROPERTY_ID = "Property_ID"
    PROPERTY = "Property"
    ADDRESS = "Address"
    RENTAL_SPACE = "Rental space" 

    def __init__ (self):
        pass



    def FetchProperties(self) -> list[Properties]: 

        """Fetching all the properties"""

        all_properties: list[Properties] = []
        with open("data_files/properties.csv", "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                all_properties.append(Properties(row[self.DEESTINATION_ID], 
                                               row[self.PROPERTY_ID],
                                               row[self.PROPERTY],
                                               row[self.ADDRESS],
                                               row[self.RENTAL_SPACE],)) 
        return all_properties
    
            


    def AddProperty(self,property:Property):
        
        """Adding a new property to the properties.csv file"""
        
        with open("data_files/properties.csv", 'a', newline='', encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([properties.property_id,
                            property.destination_id,
                            property.property,
                            property.address,
                            property.rental_space])
        return "Property added successfully"



    def delete_property(self, property: Property):   
        with open(self.filepath, 'r+') as file:
            rows = file.readlines()
            file.seek(0)
            for property_to_delete in rows:    
                if property_to_delete.strip() != format(property): #if property is not the one we want to delete we keep it by writing
                    file.write(property_to_delete)
                #if it is the property we want to delete it will not be written and truncated from file
                file.truncate()



    def update_properties(self, property: Property): #þarf að breyta í eintölu
        with open(self.filepath, 'w') as file:
            for row in reader:
                if row[]





dl_properties = DL_Properties()
properties = dl_properties.fetch_properties()
#dl_properties.add_properties(properties[0])
#dl_properties.delete_property(properties[1])


