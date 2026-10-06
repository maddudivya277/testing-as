from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open W3Schools iframe demo
    page.goto(
        "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe"
    )

    # Switch to the first iframe
    iframe = page.locator("iframe").first

    # Get the title inside the iframe
    iframe_title = iframe.content_frame.title()

    print("Page title inside iframe:", iframe_title)

    # Playwright automatically works with the main page again
    # after using the iframe object.
    print("Back to main content")

    browser.close()