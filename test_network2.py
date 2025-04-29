import time

from playwright.sync_api import Page, Playwright, expect

from Utils.apiBase2 import APIUtils


def intercept_request(route):
    route.continue_(url="https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=679fd003e2b5443b1f440f95")

def test_network(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*", intercept_request)
    page.locator("#userEmail").fill("victor@gmail.com")
    page.locator("#userPassword").fill("Jack123!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    page.get_by_role("button", name="View").first.click()
    time.sleep(5)
    order_text=page.locator(".blink_me").text_content()
    print(order_text)

def test_session_storage(playwright:Playwright):
    api=APIUtils()
    gettoken=api.getToken(playwright)
    browser=playwright.chromium.launch(headless=False)
    context=browser.new_context()
    page=context.new_page()
    page.add_init_script(f"""localStorage.setItem('token','{gettoken}')""")
    page.goto("https://rahulshettyacademy.com/client")
    page.get_by_role("button", name="ORDERS").click()
    expect(page.get_by_text('your Orders')).to_be_visible()
