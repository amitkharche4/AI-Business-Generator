# assets.py
import os
from openai import OpenAI

# ✅ Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_assets(idea):
    """Generate marketing assets (logo concept, tagline, description) for a given business idea."""
    prompt = f"""
    You are an AI marketing assistant.
    For the business idea: "{idea}"
    Generate the following:
    - A catchy brand name
    - A one-line tagline
    - A short description (2-3 sentences)
    - 3 marketing post ideas for social media

    Return as JSON:
    {{
      "brand_name": "...",
      "tagline": "...",
      "description": "...",
      "posts": ["...", "...", "..."]
    }}
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.8,
    )

    text = response.choices[0].message.content.strip()
    return text
