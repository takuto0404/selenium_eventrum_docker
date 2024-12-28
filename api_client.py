import requests
import asyncio

class ApiClient:
    BASE_URL = "http://127.0.0.1:8080"

    # データ追加（POSTリクエスト）未使用
    @classmethod
    async def add_articles(cls, genre, results):
        # tasks = [cls.add_article(genre, result) for result in results]
        tasks = cls.add_article(genre, results[0])
        await asyncio.gather(tasks)
        
    @classmethod
    async def add_article(cls, genre, result):
        data = {
            "sourceId" : result["sourceId"],
            "sourceName" : result["sourceName"],
            "author" : result["author"],
            "title" : result["title"],
            "description" : result["description"],
            "url" : result["url"],
            "urlToImage" : result["urlToImage"],
            "publishedAt" : result["publishedAt"],
            "content" : result["content"],
            "paragraphs" : result["paragraphs"]
        }
        try:
            response = await requests.post(f"{cls.BASE_URL}/articles/{genre}", json=data)
            if response.status_code == 200:
                print("Article added successfully:", response.json())
            else:
                print(f"Failed to add article. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error connecting to API: {e}")