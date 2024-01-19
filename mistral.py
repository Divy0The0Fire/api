from huggingface_hub import InferenceClient
import random
from time import time as t

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.1"


messages = [
    {"role": "system", "content": "I'm the latest J.A.R.V.I.S. AI, designed by Divyansh Shukla with capabilities to access systems through various programming languages using modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc."},
]

# Function to format prompt
def format_prompt(message, custom_instructions=None):
    prompt = ""
    if custom_instructions:
        prompt += f"[INST] {custom_instructions} [/INST]"
    prompt += f"[INST] {message} [/INST]"
    return prompt

# Function to generate response based on user input
def Mistral7B(prompt,messages:list=[{}],API_KEY="", temperature=0.9, max_new_tokens=1024, top_p=0.95, repetition_penalty=1.0):
    C=t()
    headers = {"Authorization": f"Bearer {API_KEY}"}
    temperature = float(temperature)
    if temperature < 1e-2:
        temperature = 1e-2
    top_p = float(top_p)

    generate_kwargs = dict(
        temperature=temperature,
        max_new_tokens=max_new_tokens,
        top_p=top_p,
        repetition_penalty=repetition_penalty,
        do_sample=True,
        seed=random.randint(0, 10**7),
    )
    custom_instructions=str(messages)
    formatted_prompt = format_prompt(prompt, custom_instructions)

    messages.append({"role": "user", "content": prompt})

    client = InferenceClient(API_URL, headers=headers)
    response = client.text_generation(formatted_prompt, **generate_kwargs)

    messages.append({"role": "assistant", "content": response})
    
    return response,messages,t()-C

if __name__=="__main__":
    while True:
        # Get user input
        user_prompt = input("You: ")

        # Exit condition
        if user_prompt.lower() == 'exit':
            break

        generated_text = Mistral7B(user_prompt)
        print("Bot:", generated_text)