from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.instagram.com")

    # Find the Like button through its parent post container
    like_button = page.locator(
        "//span[@class='username']/parent::div//button[contains(@class,'like')]"
    )

    print("Like button found:", like_button.count())

    browser.close()