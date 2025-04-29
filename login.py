from pytest_playwright.pytest_playwright import page
from .dashboard import Dashboardpage

class Loginpage:
    def __init__(self,page):
        self.page=page

    def navigate(self):
        self.page.goto("https://rahulshettyacademy.com/client")

    def loggingIN(self,username,password):
        self.page.locator("#userEmail").fill(username)
        self.page.locator("#userPassword").fill(password)
        self.page.get_by_role("button", name="Login").click()
        dashboardpage=Dashboardpage(self.page)
        return dashboardpage

