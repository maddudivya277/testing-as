from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.flipkart.com/")

    # Using CSS Selector
    page.locator("input[name='q']").fill("laptop")

    # OR using XPath
    # page.locator("//input[@name='q']").fill("laptop")

    page.wait_for_timeout(3000)
    browser.close()