from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.irctc.co.in/")

    # Example: select a city from a dropdown
    page.select_option("#city", label="Ahmedabad")

    page.wait_for_timeout(3000)
    browser.close()