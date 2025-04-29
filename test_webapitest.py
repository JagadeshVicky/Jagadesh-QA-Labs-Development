import time

from playwright.sync_api import Playwright, expect

from Utils.apiBase2 import APIUtils


#end to end automation testing using playwright and API
def test_endtoendwebapi(playwright:Playwright):
    browser=playwright.chromium.launch(headless=False)
    context= browser.new_context()
    page=context.new_page()

    # create order
    apiutils = APIUtils()
    orderId=apiutils.createOrder(playwright)

    #login the application :
    page.goto("https://rahulshettyacademy.com/client")
    page.locator("#userEmail").fill("rahulshetty@gmail.com")
    page.locator("#userPassword").fill("Iamking@000")
    page.get_by_role("button", name="Login").click()

    page.get_by_role("button", name="ORDERS").click()

    #order history to check the product is added
    row=page.locator("tr").filter(has_text=orderId)
    row.get_by_role("button", name="View").click()
    expect(page.locator(".tagline")).to_contain_text("Thank you for Shopping With Us")
""" page.get_by_role("button", name="Add To Cart").click()
    print("click done")
    '''page.get_by_role("button", name="ORDERS").click()
    print(orderID)

    row = page.locator("tr").filter(has_text=orderID)
    row.get_by_role("button", name="View").first.click()

    expect(page.locator(".tagline")).to_contain_text("Thank you for shopping with us")
    context.close()
    time.sleep(3)'''
    #add to cart a product
"""