import csv
import os
#from models.Properties import Properties
class Property:
    def __init__ (self):
        self.destination_id = None 
        self.property_id = None 
        self.property = None 
        self.address = None 
        self.rental_space = None 
    
    def __str__(self) -> str:
        return f"{self.destination_id}, {self.property_id}, {self.property}, {self.address}, {self.rental_space} "
        
    def __format__(self, format_spec: str) -> str:
        return f"{self.destination_id},{self.property_id},{self.property},{self.address},{self.rental_space}"



class DL_Properties():
    def __init__(self):
        self.filepath = '/Users/rakeleir/Desktop/Untitled/data_files/properties.csv' #breyta þetta virkar bara fyrir mig

    def store_properties(self, file_path): #actually hvað
        pass

    def fetch_properties(self) -> list[Property]: 
        with open(self.filepath, 'r') as file:
            rows = csv.reader(file, delimiter='\n')
            properties = self.__create_models(rows)
            return properties
    
    def fetch_property(self, property_id):
        pass
            

    def add_properties(self, property: Property):
        with open(self.filepath, 'a') as file:
            propertyString = format(property)
            file.write(propertyString) #það sem ég vil setja inn 

    def delete_property(self, property: Property):   
        with open(self.filepath, 'r+') as file:
            rows = file.readlines()
            file.seek(0)
            for property_to_delete in rows:    
                if property_to_delete.strip() != format(property): #if property is not the one we want to delete we keep it by writing
                    file.write(property_to_delete)
                #if it is the property we want to delete it will not be written and truncated from file
                file.truncate()

    def update_properties(self): #nota edit file eða??
        pass
    
    def __create_models(self,rows: list[list[str]]):
        properties: list[Property] = []
        for row in rows:   
            property = Property()
            property.destination_id = row[0].split(',')[0]
            property.property_id = row[0].split(',')[1]
            property.property = row[0].split(',')[2]
            property.address = row[0].split(',')[3]
            property.rental_space = row[0].split(',')[4]
            properties.append(property)
        return properties

dl_properties = DL_Properties()
properties = dl_properties.fetch_properties()
#dl_properties.add_properties(properties[0])
dl_properties.delete_property(properties[1])


