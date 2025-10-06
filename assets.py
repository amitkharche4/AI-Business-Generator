
from openai import OpenAI
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_assets(idea):
    prompt = f"""
    Create marketing assets for this business idea: {idea}.
    Include:
    1. Landing page copy
    2. Email copy
    3. 5 social media post ideas
    """
    client = OpenAI(api_key=openai.api_key)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    return response.choices[0].message.content
