from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from InternetManager import InternetManager
from ApiDataManager import ApiDataManager
import sys
import os
import asyncio
import json

log_file = "/home/azureuser/scripts/output.log"
sys.stdout = open(log_file, "w")
sys.stderr = open(log_file, "w")

def initialize_selenium_driver():
    options = Options()
    options.binary_location = "/usr/bin/google-chrome"
    options.add_argument("--headless")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-gpu")

    os.environ["WDM_LOCAL"] = "1"
    os.environ["WDM_CACHE_DIR"] = "/tmp"

    driver_path = ChromeDriverManager().install()
    service = ChromeService(driver_path)
    driver = webdriver.Chrome(service=service, options=options)
    return driver

async def fetch_news_data(genre_type):
    await ApiDataManager.initialize_async()
    return await InternetManager.fetch_news_data_async(genre_type)

def main():

    driver = initialize_selenium_driver()
    result_dict = {}
    try:
        genreList = ["Top","Business","Entertainment","Health","Science","Sports","Technology"]

        for i in range(len(genreList)):
            genre_type = genreList[i]
            news_json = asyncio.run(fetch_news_data(genre_type))
            news_dict = json.loads(news_json)
            
            for article in news_dict.get('articles', []):
                url = article.get("url")
                if url:
                    driver.get(url)
                    try:
                        paragraphs = list(filter(lambda x: x != "", map(lambda x: x.text, driver.find_elements(By.TAG_NAME, "p"))))
                        article['paragraphs'] = paragraphs

                    except Exception as e:
                        print(f"Failed to scrape article from {url}: {e}")
            result = json.dumps(news_dict)
            result_dict[genreList[i]] = result
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()

# videoタグのsrc
# imgタグのsrc←記事以外のやつは表示しないようにしたい