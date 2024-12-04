import csv
from models.WorkOrders import WorkOrders


class DL_WorkOrders():
    WORK_ORDER_ID = "Work_order_ID"
    EMPLOYEE = "Employee"
    CONTRACTOR = "Contractor"
    CONTRACTOR_ID = "Contractor_ID"
    PROPERTY_IDS = "Property_IDs"
    MAINTENANCE_INFO = "Maintenance_info"
    REGULAR = "Regular"
    DAYS_BETWEEN_OR_WHEN = "Days_between_or_when"
    VISIBLE = "Visible"
    OPENS = "Opens"
    FINISHED = "Finished"
    APPROVED = "Approved"
    STATE_OF_WORK_ORDER = "State_of_work_order"
    PRIORITY = "Priority"





    def __init__ (self):
        pass

    def FetchWorkOrders(self) -> list[WorkOrders]:

        all_WorkOrders: list[WorkOrders] = []
        with open("data_files/work_orders.csv", "r", newline="", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)

            for row in reader:
                all_WorkOrders.append(WorkOrders(row[self.WORK_ORDER_ID],
                                                 row[self.EMPLOYEE],
                                                 row[self.CONTRACTOR],
                                                 row[self.CONTRACTOR_ID],
                                                 row[self.PROPERTY_IDS],
                                                 row[self.MAINTENANCE_INFO],
                                                 row[self.REGULAR],
                                                 row[self.DAYS_BETWEEN_OR_WHEN],
                                                 row[self.VISIBLE],
                                                 row[self.OPENS],
                                                 row[self.FINISHED],
                                                 row[self.APPROVED],
                                                 row[self.STATE_OF_WORK_ORDER],
                                                 row[self.PRIORITY]))
        return all_WorkOrders


    def AddWorkOrders(self, workorder: WorkOrders):

        with open("data_files/work_orders.csv", "a", newline= "", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([workorder.work_order_id,
                            workorder.employee,
                            workorder.contractor,
                            workorder.contractor_id,
                            workorder.property_ids,
                            workorder.maintenance_info,
                            workorder.regular,
                            workorder.days_between_or_when,
                            workorder.visible,
                            workorder.opens,
                            workorder.finished,
                            workorder.approved,
                            workorder.state_of_work_order,
                            workorder.priority])
            
        return "Work Order added successfully"

       

    def FinishedWorkOrder(self, workorder: WorkOrders):
        workorder.finished = True
        self.UpdateWorkOrders([workorder])

    def ApprovedWorkOrder(self, workorder: WorkOrders):
        workorder.approved = True
        self.UpdateWorkOrders([workorder])



    def UpdateWorkOrders(self, update_workorders: list[WorkOrders]):


        workorders = self.FetchWorkOrders()
        with open("data_files/work_orders.csv", "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.DictWriter(csvfile, [self.WORK_ORDER_ID, self.EMPLOYEE, self.CONTRACTOR, self.CONTRACTOR_ID, self.PROPERTY_IDS, self.MAINTENANCE_INFO, self.REGULAR, self.DAYS_BETWEEN_OR_WHEN, self.VISIBLE, self.OPENS, self.FINISHED, self.APPROVED, self.STATE_OF_WORK_ORDER, self.PRIORITY])
            writer.writeheader()

            for workorder in update_workorders:
                try:
                    i = workorders.index(workorder)
                    workorders[i] = workorder
                except:
                    pass

            for workorder in workorders:
                writer.writerow({self.WORK_ORDER_ID: workorder.work_order_id,
                                 self.EMPLOYEE: workorder.employee,
                                 self.CONTRACTOR: workorder.contractor,
                                 self.CONTRACTOR_ID: workorder.contractor_id,
                                 self.PROPERTY_IDS: workorder.property_ids,
                                 self.MAINTENANCE_INFO: workorder.maintenance_info,
                                 self.REGULAR: workorder.regular,
                                 self.DAYS_BETWEEN_OR_WHEN: workorder.days_between_or_when,
                                 self.VISIBLE: workorder.visible,
                                 self.OPENS: workorder.opens,
                                 self.FINISHED: workorder.finished,
                                 self.APPROVED: workorder.approved,
                                 self.STATE_OF_WORK_ORDER: workorder.state_of_work_order,
                                 self.PRIORITY: workorder.priority})
            return update_workorders
        

