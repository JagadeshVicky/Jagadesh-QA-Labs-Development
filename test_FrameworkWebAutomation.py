import json

import pytest

from Utils.apiBase2 import APIUtils
from playwright.sync_api import Playwright

from PageObjects.login import Loginpage

with open('data/credentials.json') as j:
    data = json.load(j)
    print(data)
    user_credential_list = data['user_credetials']

@pytest.mark.parametrize('user_credetials',user_credential_list)
def test_endtoendwebapi(playwright:Playwright,user_credetials):
    username = user_credetials['user_email']
    password = user_credetials['user_password']
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()


# create order
    api_utils = APIUtils()
    orderId=api_utils.createOrder(playwright,user_credetials)

    loginpage=Loginpage(page)
    loginpage.navigate()
    Dashboardpage=loginpage.loggingIN(username,password)
    '''page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill(user_credetials["user_email"])
    page.locator("#userPassword").fill(user_credetials["user_password"])
    page.get_by_role("button", name="Login").click()'''

    orderhistorypage=Dashboardpage.selectingproduct()
    '''page.get_by_role("button", name="ORDERS").click()'''

    OrderDetailsPage=orderhistorypage.SelectOrder(orderId)
    # order history to check the product is added
    '''row = page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()'''

    OrderDetailsPage.verifyordermessage()
    #expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")

