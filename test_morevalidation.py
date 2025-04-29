from playwright.sync_api import Page, expect


def test_UIChecks(page:Page):
    #Hide/Display of placeholder function
    page.goto("http://www.rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.get_by_role("button", name="Hide").click()
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
#alert handling
    page.on("dialog", lambda dialog:dialog.accept())
    page.get_by_role("button", name="Confirm").click()
#mouse hover
    page.locator("#mousehover").hover()
    page.get_by_role("link", name="Top").click()
#iFrame handling
    PageFrame=page.frame_locator("#courses-iframe")
    PageFrame.get_by_role("link", name="All Access plan").click()
    expect(PageFrame.get_by_text(" Happy Subscibers!")).to_be_visible()

#check the price of rice = 37 or not ?
def test_loopvalidation(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")
    for index in range(page.locator("th").count()):
        if page.locator("th").nth(index).filter(has_text="Price").count()>0:
            priceColValue=index
            print(priceColValue)
            break

    ricerow=page.locator("tr").filter(has_text="Rice")
