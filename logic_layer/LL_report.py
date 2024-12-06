from models.Contractors import Contractors
from models.Report import Reports

class LL_Report:

    def __init__(self, dl_wrapper):
        self.dl_wrapper = dl_wrapper
        self.m_reports = Reports()
        self.m_contractors = Contractors()
        self.reports = dl_wrapper.get_all_reports()

    def get_my_reports(self, id_num) -> list:

        report_list = []
        for report in self.reports:
            if int(report.report_id) == id_num:
                work_order_id = report.work_order_ID
                work_done = report.work_done
                contractor_id = report.contractor_id
                additional_info = report.additional_report_info
                material_cost = report.material_cost
                contractor_cost = report.contractor_cost
                total_cost = report.total_cost
                if bool(contractor_id) == True:
                    contractors = self.dl_wrapper.get_all_contractors()
                    for contractor in contractors:
                        if report.contractor_id == contractor.contractor_id:
                            contractor_name = contractor.name
                            contact_phone = contractor.contact_phone
                            contact_name = contractor.contact_name
                            specialty = contractor.specialty
                            report_list.append([work_order_id, work_done, contractor_name, contact_phone, contact_name, specialty, additional_info, material_cost, contractor_cost, total_cost])
                else:
                    report_list.append([work_order_id, work_done, additional_info, material_cost, total_cost])

        return [["1", "ekkert :(", "tell me about it", "25876", "25876"], ["2", "slayyy", "Kalli sæti", "696 9999", "Frikki ljóti", "Málari", "Frikki ljót svarar aldrei\nsímanum, ekki hringja.", "10000", "20000", "30000"], ["3", "prump hihihihi", "aaaaaaa", "25879", "25879"]]
        return report_list
    
    def sort_my_reports(self, reports: list) -> list:
        return reports # Bara fyrir test



    def verifyReportID():
        pass

    def verifyIfFilledOut(): #Mögulega bæta svipuðu falli við í workorders
        pass

    def verifyReportInfo():
        pass

    def verifySearchReport():
        pass

    def getFilteredReport():
        pass

    def getReportID():
        pass