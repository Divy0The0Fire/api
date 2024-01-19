#pip install -U g4f
import g4f
from time import time as t


def MsgDelAuto(messages:list):
    x = len(messages.__str__())
    if x>5500:
        messages.pop(10)
        return MsgDelAuto(messages)
    else:
        return messages

def ChatGpt(message:str,messages:list=[]):
    C=t()
    messages=MsgDelAuto(messages)
    messages.append({"role": "user", "content": message})

    response = g4f.ChatCompletion.create(
        model="gpt-4-32k-0613",
        provider=g4f.Provider.GPTalk,
        messages=messages,
        stream=True,
    )
    
    ms=""
    for message in response:
        ms+=str(message)
    messages.append({"role": "assistant", "content": ms})
    
    return ms,messages,t()-C

if __name__=="__main__":

    A=input(">>> ")
    C=t()
    print(ChatGpt(A,[]))
    print(t()-C)

