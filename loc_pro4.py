from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open BookMyShow
    page.goto("https://in.bookmyshow.com/")
    page.wait_for_load_state("domcontentloaded")

    # Open the sign-up/login page
    # Click the Login button if required
    page.get_by_text("Login", exact=True).click()

    # Locate the mobile number input using its name attribute
    mobile_input = page.locator('input[name="mobile"]')
    mobile_input.fill("9876543210")

    # Find the first button element (equivalent to By.TAG_NAME, "button")
    first_button = page.locator("button").first

    # Print button text
    print("First button text:", first_button.inner_text())

    browser.close()