from selenium.webdriver import Remote, ChromeOptions
from selenium.webdriver.chromium.remote_connection import ChromiumRemoteConnection
import time
def scrape_website(website):
    print("Launching chrome broswer...")

    chrom_driver_path = ""
    options = webdriver.ChromeOptions()# type: ignore
    driver = webdriver.Chrome(service=Service(chrome_driver_path),options=options) # type: ignore

    try:
        driver.get(website)
        print("Page loaded...")
        html = driver.page_source
        time.sleep(10)

        return html
    finally:
        driver.quit()