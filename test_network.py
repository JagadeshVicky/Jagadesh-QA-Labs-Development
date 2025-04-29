from playwright.sync_api import Page
fakepayloadOrderResponse = {"data":[],"message":"no orders"}
def intercept_response(route):
    route.fulfill(
        json= fakepayloadOrderResponse
    )

def test_network(page: Page):
    page.goto("https://rahulshettyacademy.com/client")
    page.route("https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*", intercept_response)
    page.locator("#userEmail").fill("victor@gmail.com")
    page.locator("#userPassword").fill("Jack123!")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="ORDERS").click()
    order_text=page.locator(".mt-4").text_content()
    print(order_text)
