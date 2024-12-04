class Reports:
    def __init__(self, report_id: int = None, work_order_ID: int = None, work_done: str = None, contractor: bool = None, contractor_id: int = None, additional_report_info: str = None, material_cost: int = None, contractor_cost: int = None, total_cost: int = None):
        self.report_ID = report_id
        self.work_order_ID = work_order_ID
        self.work_done = work_done
        self.contractor = contractor
        self.contractor_ID = contractor_id
        self.additional_report_info = additional_report_info
        self.material_cost = material_cost
        self.contractor_cost = contractor_cost
        self.total_cost = total_cost

    def __eq__(self, other):
        return self.report_ID == other.report_id    