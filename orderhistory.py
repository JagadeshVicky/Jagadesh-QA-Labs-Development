from pytest_playwright.pytest_playwright import page

from .orderdetails import OrderDetailsPage


class Orderhistorypage:

    def __init__(self, page):
        self.page = page

    def SelectOrder(self, orderId):
        row = self.page.locator("tr").filter(has_text=orderId)
        row.get_by_role("button", name="View").click()
        orderDetails = OrderDetailsPage(self.page)
        return orderDetails