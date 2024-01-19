from flask import Flask, request, jsonify
from mistral import Mistral7B
from gpt import ChatGpt
from news import News
from datetime import datetime
from os import listdir
from web import Online_Scraper

app = Flask(__name__)


# Tracking API usage
counter={
    'Mistral7B': 0,
    'ChatGpt': 0,
    'News': 0,
    "Web": 0,
}

def Load():
    global counter
    current_datetime = datetime.now()

    # Extract only the date
    current_date = str(current_datetime.date())
    file=listdir(r"static/data/")
    if current_date in file:
        with open(r"static/data/"+current_date,"r") as f:
            counter=eval(f.read())
    else:
        counter={
            'Mistral7B': 0,
            'ChatGpt': 0,
            'News': 0,
            "Web": 0,
        }
        with open(r"static/data/"+current_date,"w") as f:
            f.write(str(counter))

def Update():
    # Get the current date and time
    global counter
    current_datetime = datetime.now()

    # Extract only the date
    current_date = str(current_datetime.date())
    file=listdir(r"static/data/")
    if current_date in file:
        with open(r"static/data/"+current_date,"w") as f:
            f.write(str(counter))
    else:
        counter={
            'Mistral7B': 0,
            'ChatGpt': 0,
            'News': 0,
            "Web": 0,
        }
        with open(r"static/data/"+current_date,"w") as f:
            f.write(str(counter))

@app.route('/mistral7b', methods=['POST'])
def generate():
    global counter
    # Get data from the request
    data = request.json
    prompt = data.get('prompt', '')
    messages = data.get('messages', [])
    key = data.get('key', '')
    
    # Call Mistral7B function
    response, updated_messages, execution_time = Mistral7B(prompt, messages,key)

    # Prepare the response
    result = {
        'response': response,
        'messages': updated_messages,
        'execution_time': execution_time
    }
    counter['Mistral7B']+=1
    Update()
    return jsonify(result)

@app.route('/chatgpt', methods=['POST'])
def chat():
    global counter
    # Get data from the request
    data = request.json
    user_message = data.get('message', '')
    messages = data.get('messages', [])

    # Call ChatGpt function
    response, updated_messages, execution_time = ChatGpt(user_message, messages)

    # Prepare the response
    result = {
        'response': response,
        'messages': updated_messages,
        'execution_time': execution_time
    }
    counter["ChatGpt"]+=1
    Update()
    return jsonify(result)

@app.route('/news', methods=['GET'])
def get_news():
    global counter
    # Get data from the request
    key = request.args.get('key', '')
    cache_flag = request.args.get('cache', 'True').lower() == 'true'

    # Call News function
    news, error, execution_time = News(key, cache_flag)

    # Prepare the response
    result = {
        'news': news,
        'error': error,
        'execution_time': execution_time
    }
    counter["News"]+=1
    Update()
    return jsonify(result)

@app.route('/web', methods=['GET'])
def Web():
    key = request.args.get('prompt', '')
    counter["Web"]+=1
    return jsonify(Online_Scraper(key))


@app.route('/d0dd81747eec4c9454b2b6fe64b865e0250ed33e421c8ed6406817d0ed574770', methods=['GET'])
def get_counters():
    global counter
    return jsonify(counter),jsonify({"data":listdir(r"static/data/")})

Load()

if __name__ == '__main__':
    app.run()
