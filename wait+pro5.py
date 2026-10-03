from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.irctc.co.in/")

    # Enter journey details
    page.locator("input[placeholder*='From']").fill("Delhi")
    page.locator("input[placeholder*='To']").fill("Mumbai")

    # Click Search
    page.get_by_role("button", name="Search").click()

    # Explicit wait for train results
    train_results = page.locator(".train-list")

    train_results.wait_for(
        state="visible",
        timeout=15000
    )

    print("Train results loaded successfully.")

    browser.close()