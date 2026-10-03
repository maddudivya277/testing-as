from playwright.sync_api import sync_playwright, TimeoutError

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.zomato.com")

    try:
        # Trying to find a non-existent element
        page.locator("#non_existent_id").wait_for(timeout=5000)

        print("Element found!")

    except TimeoutError:
        print("Custom Error: Element with the given locator was not found.")

    browser.close()