class UI_Contractors:

    def __init__(self, LL_contractors):
        """initialize UI layerinn fyrir contractors"""
        self.ll_contractors == LL_contractors


    def displayContractors(self, contractors):
        """List of contractors"""
        #contractors = self.contractor_logic_layer.DL.wrapper.FetchContractors() 
        #frekar að sækja frá wrappernum?
        if not contractors:
            print("No contractors found")
            return
        for contractor in contractors:
            print(f"Contractor ID: {contractor['Contractor_ID']}, Name: {contractor['Name']}, Company{contractor: ['Company']}, Contact_phone: {contractor['Contact_phone']}, Contact_name: {contractor['Contact_name']}, Specialty: {contractor['Specialty']}, Opening_hours: {contractor['Opening_hours']}, Address: {contractor['Address']}, Former_jobs: {contractor['Former_jobs']}")
        #Þarf að taka út einhverja upplýsingar


    def displayContractorInfo(self, contractor):
        if contractor:
                print(f"Contractor ID: {contractor['Contractor_ID']}")
                print(f"Name: {contractor['Name']}")
                print(f"Company{contractor['Company']}")
                print(f"Contact_phone: {contractor['Contact_phone']}")
                print(f"Contact_name: {contractor['Contact_name']}")
                print(f"Specialty: {contractor['Specialty']}")
                print(f"Opening_hours: {contractor['Opening_hours']}")
                print(f"Address: {contractor['Address']}")
                print(f"Former_jobs: {contractor['Former_jobs']}")
        else:
            print("Contractor not found")


    def searchForContractor(self, contractors):
        print("Search contractors by: ")
        print("1. Name")
        print("2. Specialty")

        choice = input("Enter your choice: ")

        search = {}

        if choice == "1":
            Name = input("Enter contractors name: ")
            search['Name'] = Name
        elif choice == "2":
            Specialty = input("Enter contractors specialty: ")
            search['Specialty'] = Specialty
        else:
            print("Contractor not found")
            return 
        if contractors:
            print (f"{'ID':<10}{'Name':<20}{'Specialty':<15}")
            for contractor in contractors:
                print (f"{contractors.Contractor_ID:<10}{contractor.Name:<20}{contractor.Specialty:<15}")
        else: 
            print("No contractors match your search criteria.")
            
    
        
        
    def changeContractorInfo():
        pass



    def fillNewContractorForm():
        pass