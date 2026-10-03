from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Zomato homepage
    page.goto("https://www.zomato.com/")
    page.wait_for_load_state("domcontentloaded")

    # Locate "Add restaurant" link and click it
    page.get_by_role("link", name="Add restaurant").click()

    browser.close()