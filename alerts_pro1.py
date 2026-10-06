from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Myntra
    page.goto("https://www.myntra.com/")
    page.wait_for_load_state("domcontentloaded")

    # Handle JavaScript alert
    def handle_dialog(dialog):
        print("Alert message:", dialog.message)

        # Accept the alert
        dialog.accept()

    page.on("dialog", handle_dialog)

    # Trigger JavaScript alert
    page.evaluate('alert("Welcome to Myntra Offers!")')

    print("Alert accepted successfully")

    page.wait_for_timeout(3000)
    browser.close()