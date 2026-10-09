import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

def battle(prompt):
    msgs = [{"role": "user", "content": prompt}]

    # Model A OpenAI/gpt-oss-120b - on_demand
    a = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=msgs,
    )

    # Model B qwen/qwen3.8-27b - on_demand
    b = client.chat.completions.create(
        model="qwen/qwen3.8-27b",
        messages=msgs,
    )

    return a.choices[0].message.content, b.choices[0].message.content

