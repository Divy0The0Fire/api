import requests

url_mistral7b = "http://127.0.0.1:5000/mistral7b"

data_mistral7b = {
    "prompt": "Your prompt here",
    "messages": [{"role": "user", "content": "Previous user message"}],
    "key": "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"
}

response_mistral7b = requests.post(url_mistral7b, json=data_mistral7b)
print(response_mistral7b.json())


import requests

url_chatgpt = "http://127.0.0.1:5000/chatgpt"

data_chatgpt = {
    "message": "Your user message here",
    "messages": [{"role": "user", "content": "Previous user message"}]
}

response_chatgpt = requests.post(url_chatgpt, json=data_chatgpt)
print(response_chatgpt.json())



import requests

url_news = "http://127.0.0.1:5000/news"

params_news = {
    "key": "5b57a2e4baa74123b6db7dff6967881b",
    "cache": "true"
}

response_news = requests.get(url_news, params=params_news)
print(response_news.json())
