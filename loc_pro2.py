from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.flipkart.com/")
    page.wait_for_load_state("domcontentloaded")

    # Find all elements with class name 'btn'
    buttons = page.locator(".btn").all()

    # Print the text of each button
    for button in buttons:
        print(button.inner_text())

    browser.close()