from selenium import webdriver
from selenium.webdriver.common.by import By
from InternetManager import InternetManager
from ApiDataManager import ApiDataManager
from api_client import ApiClient
from datetime import datetime
import asyncio
import json

def initialize_selenium_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    driver = webdriver.Remote(
        command_executor='https://standalone-chromium-latest-gr3h.onrender.com/wd/hub',  # コンテナの Selenium Hub に接続
        options=options,  # options を渡す
    )
    return driver

async def fetch_news_data(genre_type):
    await ApiDataManager.initialize_async()
    return await InternetManager.fetch_news_data_async(genre_type)

async def scrape_article(driver, article):
    url = article.get("url")
    if url:
        try:
            driver.get(url)
            paragraphs = [element.text for element in driver.find_elements(By.TAG_NAME, "p") if element.text.strip()]
            article['paragraphs'] = paragraphs

            video_elements = driver.find_elements(By.TAG_NAME, "video")
            article['videos'] = [video.get_attribute("src") for video in video_elements if video.get_attribute("src")]

            image_elements = driver.find_elements(By.TAG_NAME, "img")
            article['images'] = [img.get_attribute("src") for img in image_elements if img.get_attribute("src")]
        except Exception as e:
            print(f"Failed to scrape article from {url}: {e}")
    return article

def get_lastTimeUpdated():
    f = open('lastTimeUpdated.txt')
    dateTimeString = f.read()
    return datetime.fromisoformat(dateTimeString.replace("Z", "+00:00"))

def update_lastTimeUpdated(time):
    f = open('lastTimeUpdated.txt', 'w')
    f.write(time)


async def process_genre(driver, genre_type):
    news_json = await fetch_news_data(genre_type)
    news_dict = json.loads(news_json)
    articles = news_dict.get('articles', [])

    last_time_updated = get_lastTimeUpdated()

    filtered_articles = [
        article for article in articles
        if datetime.fromisoformat(article["publishedAt"].replace("Z", "+00:00")) > last_time_updated
    ]
    update_lastTimeUpdated(filtered_articles[-1].get('publishedAt'))

    tasks = scrape_article(driver, filtered_articles[0])
    results = await asyncio.gather(tasks)
    # tasks = [scrape_article(driver, article) for article in articles]
    # await asyncio.gather(*tasks)

    await ApiClient.add_articles(genre_type, results)

# async def main():
async def main():
    driver = initialize_selenium_driver()
    # try:
    #     genre_list = ["Top", "Business", "Entertainment", "Health", "Science", "Sports", "Technology"]
    #     result_dict = {}
    #
    #     tasks = process_genre(driver, "Top")
    #     await asyncio.gather(tasks)
    #     # tasks = [process_genre(driver, genre) for genre in genre_list]
    #     # await asyncio.gather(*tasks)
    #
    # except Exception as e:
    #     print(f"An error occurred: {e}")
    #
    # finally:
    #     driver.quit()

if __name__ == "__main__":
    asyncio.run(main())


