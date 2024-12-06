class UI_WorkOrder:
    

    def __init__(self, LL_WorkOrders):
        self.ll_workorders = LL_WorkOrders



    def displayWorkOrders(self, workorders):
        if not workorders:
            print("No work orders found")
            return 
        for workorder in workorders:
            print(f"Work Order ID: {workorder["Work_order_ID"]}")



    def displayWorkOrderInfo(self, workorders):
        if workorders:
            print(f"Work Order ID: {workorders["Work_order_ID"]}")
            print(f"Employee: {workorders["Employee"]}")
            print(f"Contractor: {workorders["Contractor"]}")
            print(f"Contractor ID: {workorders["Contractor_ID"]}")
            print(f"Property IDs: {workorders["Property_IDs"]}")
            print(f"Maintenance info: {workorders["Maintenance_info"]}")
            print(f"Regular: {workorders["Regular"]}")
            print(f"Days between or when: {workorders["Days_between_or_when"]}")
            print(f"Visible: {workorders["Visible"]}")
            print(f"Opens: {workorders["Opens"]}")
            print(f"Finished: {workorders["Finished"]}")
            print(f"Approved: {workorders["Approved"]}")
            print(f"State of work order: {workorders["State_of_work_order"]}")
            print(f"Priority: {workorders["Priority"]}")
        else:
            print("Work order not found")



    def searchForWorkOrder(self):
            search_value = input("Work Order ID: ")
            if not search_value:

                print("You have to enter a valid work order ID:")
                return
            if not search_value.isdigit():
                print("The work order ID must be a valid integer.")
                return
            
            search_value = int(search_value)

            all_workorders = self.ll_workorders.get_all_work_orders()
            matching_workorders = []

            for workorder in all_workorders:
                if workorder['Work_order_ID'] == search_value:
                    matching_workorders.append(workorder)

            if matching_workorders:
                for workorder in matching_workorders:
                    self.displayWorkOrderInfo(workorder)
            else:
                print(f"No work order found with ID: {search_value}")


                #Samkvæmt kröfulista - það sem þarf að vera hægt að leita: 
                #yfirmaður - leitað eftir verkbeiðni samkvæmt ID hennar - KOMIÐ
                #yfirmaður - fundið allar verkbeiðnir fyrir ákveðna fasteign - ÆTTI KANNSKI AÐ VERA Í UI PROPERTY??
                #yfirmaður - fundið allar verkbeiðnir sem unnar eru af ákveðnum starfsmanni - ÞURFUM AÐ FINNA ÚT HVAR ÞETTA ÆTTI AÐ VERA



    def selectWorkOrder(self):
            search_value = input("Enter the work order ID to select: ")

            if not search_value:
                print("You must enter a valid work order ID.")
                return
            
            if not search_value.isdigit():
                print("The work order ID must be a valid integer.")
                return 
            
            search_value = int(search_value)

            all_workorders = self.ll_workorders.get_all_work_orders()

            matching_workorders = [workorder for workorder in all_workorders if workorder["Work_order_ID"] == search_value]

            if matching_workorders:
                 for workorder in matching_workorders:
                      self.displayWorkOrderInfo(workorder)
            else: 
                 print(f"No work order found with ID: {search_value}")

                #Samkvæmt kröfulista - það sem þarf að vera hægt að velja:
                 #starfsmaður - valið verkbeiðni til að vinna í - A krafa - ÆTTI AÐ VERA Í EMPLOYEE
                 #starfsmaður - valið úr verkbeiðni sem á eftir að úthluta - C krafa - ÆTTI AÐ VERA Í EMPLOYEE


  


#Kröfulisti - allt sem tengist verkbeiðnum:
#yfirmaður - listað verkbeiðnir 
#yfirmaður - stofnað nýja verkbeiðni fyrir mínar fasteignir 
#yfirmaður - breytt verkbeiðni fyrir mínar fasteignir 
#starfsmaður - merkt verkbeiðnir sem tilbúna fyrir lokun af yfirmanni 
#yfirmaður - lokað mínum verkbeiðnum
#B - krafa - yfirmaður - sett forgang á útistandandi verkbeiðnir 
#B - krafa - yfirmaður - breytt forgang á útistandandi verkbeiðnir, en þó ekki eftir skil 
#C - krafa - starfsmaður - stöðvað verkbeiðnir tímabundið og haldið síðan áfram 


#Má ekki hafa .strip() en má hafa .isdigit()?

   


"""
    def fileReportOnOrder():
        pass

    def markOrderAsFinished():
        pass

    def approveWorkOrder():
        pass

    def changeWorkOrder():
        pass

    def fillWorkOrderForm():
        pass
        
"""



