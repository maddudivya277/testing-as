from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open demo page
    page.goto("https://the-internet.herokuapp.com/javascript_alerts")

    # Handle the confirm dialog
    def handle_dialog(dialog):
        print("Dialog message:", dialog.message)

        # Dismiss the confirm dialog
        dialog.dismiss()

    page.on("dialog", handle_dialog)

    # Click "Click for JS Confirm"
    page.get_by_role("button", name="Click for JS Confirm").click()

    # Verify the result
    result = page.locator("#result").text_content()
    print("Result:", result)

    browser.close()