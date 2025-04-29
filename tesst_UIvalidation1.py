import time
from playwright.sync_api import Page, expect


def test_UIvalidationdynamicscript(page:Page):
    page.goto("http://www.rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learning")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    phone =page.locator("app-card").filter(has_text="Iphone X")
    phone.get_by_role("button",name="Add").click()
    Nokia=page.locator("app-card").filter(has_text="Nokia Edge")
    Nokia.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    #time.sleep(5)
    expect(page.locator(".media-body")).to_have_count(2)

def test_childpagehandling(page:Page):
    page.goto("http://www.rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newpage_info:
        page.get_by_text("ResumeAssistance").click()
        childpage = newpage_info.value
        text= childpage.locator(".red").text_content()
        print(text) #Please email us at mentor@rahulshettyacademy.com with below template to receive response
        text.split("at")
        email=text[0].strip().split(" ")[1]
        #assert email=="mentor@rahulshettyacademy.com"
        print("the exact value is", email)
        time.sleep(3)