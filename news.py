import requests
from time import time as t
import shelve

CACHE_FILE = "news_cache.db"

def get_cached_news():
    with shelve.open(CACHE_FILE) as cache:
        if "news" in cache:
            last_update_time = cache["last_update_time"]
            current_time = t()
            if current_time - last_update_time < 12 * 60 * 60:  # 12 hours in seconds
                return cache["news"]

    return None

def cache_news(news):
    with shelve.open(CACHE_FILE) as cache:
        cache["news"] = news
        cache["last_update_time"] = t()

def News(KEY,cache=True):
    if cache:
        cached_news = get_cached_news()
        if cached_news:
            return cached_news, None, 0  # Return cached news

    C = t()
    main_url = f'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey={KEY}'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head = []
    day = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
    for ar in articles:
        head.append(ar["title"])
    temp = []
    for i in range(len(day)):
        temp.append(f"today's {day[i]} news is: {head[i]}\n")
    result = "".join(temp)

    cache_news(result)  # Cache the news
    return result, None, t() - C

if __name__ == "__main__":
    print(News("5b57a2e4baa74123b6db7dff6967881b"))
