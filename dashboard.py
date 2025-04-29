from .orderhistory import Orderhistorypage


class Dashboardpage:
    def __init__(self,page):
        self.page=page

    def selectingproduct(self):
        self.page.get_by_role("button", name="ORDERS").click()
        orderHistory= Orderhistorypage(self.page)
        return orderHistory