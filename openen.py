import os
# pip install python-dotenv
from dotenv import load_dotenv

# pip install openai
from openai import OpenAI
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

response = client.chat.completions.create(
    model="qwen/qwen3.8-27b",
    messages=[
        {"role": "system", "content": "You are a witty travel guide."},
        {"role": "user", "content": "Suggest one thing to do in Bengalore"}
    ]
)

print(response.choices[0].message.content)