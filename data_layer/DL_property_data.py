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
        


class DL_Properties():
    def __init__(self):
        self.filepath = '/Users/rakeleir/Desktop/Untitled/data_files/properties.csv'

    def store_properties(self, file_path):
        """Load properties from a CSV file into the dictionary """
    
    def fetch_properties(self) -> list[Property]: 
        print(os.listdir)
        with open(self.filepath, 'r') as file:
            rows = csv.reader(file, delimiter='\n')
            properties = self.__create_models(rows)
            return properties
            
            

    def add_properties(self):
        pass
    def delete_properties(self):   
        pass
    def update_properties(self):
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


