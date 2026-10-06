from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Zomato
    page.goto("https://www.zomato.com")

    # Replace these locators with the actual checkbox locators
    veg_checkbox = page.locator("input[type='checkbox'][value='veg']")
    nonveg_checkbox = page.locator("input[type='checkbox'][value='nonveg']")

    # Toggle Veg Only checkbox
    veg_checkbox.check()
    print("Veg Only checked:", veg_checkbox.is_checked())

    veg_checkbox.uncheck()
    print("Veg Only checked after uncheck:", veg_checkbox.is_checked())

    # Toggle Non-Veg checkbox
    nonveg_checkbox.check()
    print("Non-Veg checked:", nonveg_checkbox.is_checked())

    nonveg_checkbox.uncheck()
    print("Non-Veg checked after uncheck:", nonveg_checkbox.is_checked())

    page.wait_for_timeout(3000)
    browser.close()