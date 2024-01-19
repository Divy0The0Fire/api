import requests
from bs4 import BeautifulSoup
from time import time as t

classes=["zCubwf","hgKElc","LTKOO sY7ric","Z0LcW","gsrt vk_bk FzvWSb YwPhnf","pclqee","tw-Data-text tw-text-small tw-ta",
    "IZ6rdc","O5uR6d LTKOO","vlzY6d","webanswers-webanswers_table__webanswers-table",
    "dDoNo ikb4Bb gsrt","sXLaOe","LWkfKe","VQF4g","qv3Wpe","kno-rdesc"]

useragent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

#scrape data from google search results
def Online_Scraper(query,PRINT=True):
    C=t()
    query=query.replace(" + "," plus ")
    query=query.replace(" - "," minus ")   
    URL = "https://www.google.co.in/search?q=" + query
    headers = {'User-Agent': useragent}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for i in classes:
        try:
            result=soup.find(class_=i).get_text()
            if PRINT:
                print(f"by class {i}")
            return result,None,t()-C
        except Exception:
            pass
    return None,None,t()-C

if __name__=="__main__":

    A=["who is iron man","spider man","78 + 98","pizza"]
    for i in A:
        C=t()
        print(Online_Scraper(i))
        print(t()-C)