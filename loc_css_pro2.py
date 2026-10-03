from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.zomato.com")

    # First restaurant name using XPath
    restaurant_name = page.locator("(//h4[text()])[1]").text_content()

    print("First Restaurant:", restaurant_name)

    browser.close()