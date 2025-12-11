import os

from playwright.sync_api import sync_playwright


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        # Construct absolute path to the local file
        cwd = os.getcwd()
        file_path = f"file://{cwd}/nhl/index.html"

        print(f"Navigating to: {file_path}")
        page.goto(file_path)

        # Wait for content to load
        page.wait_for_selector("body")

        # Screenshot the Command Hub
        screenshot_path = "verification/command_hub.png"
        page.screenshot(path=screenshot_path, full_page=True)
        print(f"Screenshot saved to {screenshot_path}")

        browser.close()


if __name__ == "__main__":
    run()
