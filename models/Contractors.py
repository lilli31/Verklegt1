class Contractors:
    def __init__(self, contractor_id: int = None, name: str = None, company: bool = None, contact_phone: int = None, contact_name: str = None, specialty: str = None, opening_hours: str = None, address: str = None, former_jobs: dict = None):
        self.contractor_id = contractor_id
        self.name = name
        self.company = company
        self.contact_phone = contact_phone
        self.contact_name = contact_name
        self.specialty = specialty
        self.opening_hours = opening_hours
        self.address = address
        self.former_jobs = former_jobs

    def __eq__(self,other):
        return self.contractor_id == other.contractor_id


      
    