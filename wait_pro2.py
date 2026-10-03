from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open Zomato
    page.goto("https://www.zomato.com/")
    page.wait_for_load_state("domcontentloaded")

    # Click Login
    page.get_by_text("Log in", exact=True).click()

    # Enter phone number
    phone_input = page.locator("input[type='tel']")
    phone_input.fill("9876543210")

    # Click Continue / Send OTP
    page.get_by_role("button", name="Continue").click()

    # Explicitly wait for OTP field
    otp_input = page.locator("input").filter(has=page.locator(""))
    # Replace the selector below with the OTP input selector found in DevTools
    page.locator("input[placeholder*='OTP']").wait_for(
        state="visible",
        timeout=10000
    )

    print("OTP field is visible")

    browser.close()