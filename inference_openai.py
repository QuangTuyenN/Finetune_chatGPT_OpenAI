from openai import OpenAI
import os
from apikey import OPENAI_API_KEY
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
client = OpenAI()

completion = client.chat.completions.create(
  model="ft:gpt-3.5-turbo-0125:personal::9eIFCaA1",
  messages=[
    {"role": "system", "content": "Bạn là chatbot phục vụ cho Thaco."},
    {"role": "user", "content": "THACO đã tham gia những hoạt động xã hội nào"}
  ]
)
print(completion.choices[0].message)

