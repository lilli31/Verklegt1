
class WorkOrders: 
    def __init__ (self, work_order_id: str = None, employee: str = None, contractor: str = None, contractor_id: int = None, property_ids: int = None, maintenance_info: str = None, regular: bool = None, days_between_or_when: int = None, visible: bool = None, opens: int = None, finished: bool = None, approved: bool = None, state_of_work_order: str = None, priority: str = None):
        self.work_order_id = work_order_id 
        self.employee = employee
        self.contractor = contractor 
        self.contractor_id = contractor_id
        self.property_ids = property_ids
        self.maintenance_info = maintenance_info
        self.regular = regular
        self.days_between_or_when = days_between_or_when
        self.visible = visible
        self.opens = opens
        self.finished = finished
        self.approved = approved
        self.state_of_work_order = state_of_work_order
        self.priority = priority

