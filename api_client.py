import requests
import asyncio

class ApiClient:
    BASE_URL = "http://127.0.0.1:8080"

    # データ追加（POSTリクエスト）未使用
    @classmethod
    async def add_articles(cls, genre, results):
        # tasks = [cls.add_article(genre, result) for result in results]
        datas = [cls.toJson(result) for result in results]
        try:
            response = await requests.post(f"{cls.BASE_URL}/articles/{genre}", json=datas)
            if response.status_code == 200:
                print("Article added successfully:", response.json())
            else:
                print(f"Failed to add article. Status code: {response.status_code}")
        except requests.RequestException as e:
            print(f"Error connecting to API: {e}")

        
    @classmethod
    def toJson(cls, result):
        data = {
            "sourceId" : result.get("sourceId"),
            "sourceName" : result.get("sourceName"),
            "author" : result.get("author"),
            "title" : result.get("title"),
            "description" : result.get("description"),
            "url" : result.get("url"),
            "urlToImage" : result.get("urlToImage"),
            "publishedAt" : result.get("publishedAt"),
            "content" : result.get("content"),
            "paragraphs" : result.get("paragraphs"),
            "videos" : result.get("videos"),
            "images" : result.get("images")
        }
        return data