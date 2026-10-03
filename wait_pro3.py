
from playwright.sync_api import sync_playwright
import time

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    # Open BookMyShow
    page.goto("https://in.bookmyshow.com/")
    page.wait_for_load_state("domcontentloaded")

    # Fluent wait configuration
    timeout = 15          # Maximum wait time: 15 seconds
    polling_interval = 0.5  # Check every 0.5 seconds

    movie_selector = "a[href*='/movies/']"

    start_time = time.time()

    while time.time() - start_time < timeout:
        movies = page.locator(movie_selector)

        if movies.count() >= 3:
            print("Movies loaded!")
            break

        time.sleep(polling_interval)
    else:
        print("Timeout: Movies did not load.")
        browser.close()
        exit()

    # Print first 3 movie names
    for i in range(3):
        movie_name = movies.nth(i).inner_text().strip()
        print(f"Movie {i + 1}: {movie_name}")

    browser.close()