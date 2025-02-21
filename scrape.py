from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeatifulSoup, BeautifulSoup
import time
def scrape_website(website):
    print("Launching Chrome browser...")

    chrom_driver_path = "./chromedriver.exe"  # Ensure this path is correct
    options = webdriver.ChromeOptions()
    
    # Pass the correct Service instance
    service = Service(chrom_driver_path)
    driver = webdriver.Chrome(service=service, options=options) 

    try:
        driver.get(website)
        print("Page loaded...")
        time.sleep(10)  # Allow time for the page to load
        return driver.page_source
    finally:
        driver.quit()

def extract_body_content(html_content):
    soup = BeautifulSoup(html_content,"html.parser")
    body_content = soup.body
    if body_content:
        return str(body_content)
    return ""
def clean_body_content(body_content):
    soup = BeautifulSoup(body_content,"html.parser")

    for script_or_style in soup(["script","style"]):
        script_or_style.extract()

    cleaned_content = soup.get_text(seperator="/n")
    cleaned_content = "/n".join(
        line.strip() for line in cleaned_content.splitline() if line.strip()
     )