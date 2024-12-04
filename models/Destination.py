class Destination:
    def __init__(self, destination_ID: int = None, country: str = None, destination: str = None):
        self.destination_ID = destination_ID
        self.country = country
        self.destination = destination
        
    def __eq__(self, other):
        return self.destination_ID == other.destination_ID    