import requests
from dotenv import load_dotenv
import os
import sys

keywords = sys.argv[1:]

url = "https://eventregistry.org/api/v1/article/getArticles"
load_dotenv()
api_key = os.getenv("NEWS_API_KEY")

payload = {
  "action": "getArticles",
  "keyword": keywords,
  "keywordOper": "and",
  "lang": ["eng"],
  "startSourceRankPercentile": 0,
  "endSourceRankPercentile": 30,
  "articlesCount": 1,
  "articlesSortBy": "rel",
  "includeArticleConcepts": True,
  "includeArticleCategories": True,
  "includeArticleImage": True,
  "includeArticleSocialScore": True,
  "includeArticleLocation": True,
  "resultType": "articles",
  "apiKey": api_key,
  "forceMaxDataTimeWindow": 31
}

response = requests.post(url, json=payload)

if response.status_code == 200:
    data = response.json()
    articles = data["articles"]["results"]

    first = articles[0]

    print(first["title"])
    print(first["source"])
    print(first["body"])
    print(first["date"])
    print(first["url"])

else:
    print("Błąd:", response.status_code)