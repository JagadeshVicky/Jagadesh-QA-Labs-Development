import time
from idlelib import browser
from playwright.sync_api import Page, expect, Playwright


def test_playwrightbasics(playwright):
    # Launch the browser
    browser = playwright.chromium.launch(headless=False)
    # Create a new browser context
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.facebook.com/")

def test_playwrightshrtcuts(page:Page):
    page.goto("https://www.facebook.com/")

def test_automatewebapplication(page:Page):
    page.goto("http://www.rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningfd")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)

def test_firefoxbrowser(playwright:Playwright):
    firefoxbrowser=playwright.firefox
    browser=firefoxbrowser.launch(headless=False)
    page = browser.new_page()
    page.goto("http://www.rahulshettyacademy.com/loginpagePractise/")
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("learningfd")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()
    page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    time.sleep(5)
