from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Myntra
    page.goto("https://www.myntra.com/")

    # Wait until the Myntra logo is visible
    logo = page.locator("a[href='/']")
    logo.wait_for(state="visible", timeout=10000)

    print("Myntra logo is visible")

    # Click Men menu
    page.get_by_text("Men", exact=True).first.click()

    print("Men menu clicked")

    browser.close()