from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
from datetime import datetime


def wait_for_datadome_captcha(page, timeout=300):
    """
    Waits for the DataDome CAPTCHA iframe to disappear.
    """
    print("🛑 CAPTCHA detected (DataDome). Please solve it manually in the browser...")

    elapsed = 0
    while elapsed < timeout:
        # Check if the CAPTCHA iframe is still there
        print("Time remaining to solve:", timeout - elapsed, "seconds")
        try:
            if not page.is_visible('iframe[src*="captcha-delivery.com"]', timeout=1000):
                print("✅ CAPTCHA cleared. Continuing...")
                return
        except:
            pass  # Element not found or already removed

        time.sleep(2)
        elapsed += 2

    raise TimeoutError("⏰ CAPTCHA was not solved within the timeout period.")


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # Set to True for headless mode
    page = browser.new_page()
    page.goto("https://www.reuters.com/", wait_until="domcontentloaded")

    if page.locator('iframe[src*="captcha-delivery.com"]').is_visible():
        wait_for_datadome_captcha(page)

    # Wait for the page to load
    page.wait_for_timeout(5000)

    html = page.content()  # Get rendered HTML
    with open(f"html/reuters_{datetime.now()}.html", "w+") as f:
        bs = BeautifulSoup(html, "html.parser")
        f.write(bs.prettify())
    browser.close()
