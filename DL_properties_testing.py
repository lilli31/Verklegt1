from data_layer.DL_properties_data import DL_Properties
from models.Properties import Properties


data_layer = DL_Properties()

pro_data = data_layer.FetchProperties()
for property in pro_data:
    print(property.address)


new_property = Properties("4", "Nyg11", "Hotel Mud", "Rakel", "1")

try:
    result = data_layer.AddProperty(new_property)
    print(result) 
    
except Exception as p:
    print("An error occurred during testing:")

new_property.property_ID = "19"
new_property.address = "kiki"


try:
    result = data_layer.UpdateProperties(new_property)
    print([r.name for r in result]) 
    
except Exception as p:
    print("An error occurred during testing:")
    print(p)

    print("An error occurred during testing:", p)