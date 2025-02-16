import aiohttp
import asyncio
from ApiDataManager import ApiDataManager

class InternetManager:
    @classmethod
    async def fetch_news_data_async(cls, genre_type, keyword=""):
        try:
            url = cls.get_url(keyword, genre_type)
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        result = await response.text()
                        return result
                    else:
                        print(f"Request failed with status {response.status}")
        except asyncio.CancelledError:
            print("Request was cancelled")
        except Exception as e:
            print(f"An error occurred: {e}")

    @classmethod
    def get_url(cls, keyword, genre_type):
        country_code = ApiDataManager.get_country_code()
        country_text = f"country={country_code}&"
        category_text = "" if genre_type == "top" else f"category={ApiDataManager.get_genre_code(genre_type)}&"
        query_text = f"q={keyword}&" if keyword else ""
        api_key = ApiDataManager.APIKey
        return f"https://newsapi.org/v2/top-headlines?{country_text}{category_text}{query_text}apiKey={api_key}"
