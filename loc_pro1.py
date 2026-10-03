from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.myntra.com/login")

    # Locate the email/phone input using its ID
    email_field = page.locator("#mobileNumber")

    # Enter your college email
    email_field.fill("your_college_email@example.com")

    browser.close()