from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://www.flipkart.com/")

    # ... search for a product and open the product page ...

    # Instead of: time.sleep(5)
    # Explicitly wait for Add to Cart button
    add_to_cart = page.get_by_text("Add to cart", exact=True)

    add_to_cart.wait_for(state="visible", timeout=10000)

    # Click when the button is actionable
    add_to_cart.click()

    print("Product added to cart")

    browser.close()