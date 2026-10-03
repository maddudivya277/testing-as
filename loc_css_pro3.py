from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.myntra.com")

    # Relative XPath (recommended)
    login_btn = page.locator("//a[contains(text(),'Login') or contains(text(),'Sign In')]")
    print(login_btn.count())

    browser.close()