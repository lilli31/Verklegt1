from data_layer.DL_contractors_data import DL_Contractor
from models.Contractors import Contractors

data_layer = DL_Contractor()

con_data = data_layer.FetchContractors()
for contractor in con_data:
    print(contractor.contact_phone)

new_contractor = Contractors("2", "Atli", "apple", "Atli Jóns", "+354 888-9999", "Tölvur",
                         "08:00-16:00","Grundavegur 3", "Sjoppa")

try:
    result = data_layer.AddContractors(new_contractor)
    print(result) 
    
except Exception as c:
    print("An error occurred during testing:", c)

new_contractor.contractor_id = "4"
new_contractor.address = "Biggastræti"

try:
    result = data_layer.UpdateContractors([new_contractor])
    print([r.name for r in result]) 
    
except Exception as c:
    print("An error occurred during testing:")
    print(c)

    print("An error occurred during testing:", c)