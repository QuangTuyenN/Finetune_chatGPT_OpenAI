from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from apikey import OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

model_name = "ft:gpt-3.5-turbo-0125:personal::9eIFCaA1"
chat = ChatOpenAI(model=model_name)

while True:
    nhap = input("Q: ")
    rep = chat(messages=[HumanMessage(content=f"{nhap}")])
    print("A: ", rep.content)




