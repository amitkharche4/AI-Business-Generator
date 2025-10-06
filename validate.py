# validate.py
import os
from openai import OpenAI

# ✅ Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_idea(idea):
    """
    Validate the market potential of a business idea.
    Returns a score from 1–10 and a short explanation.
    """
    prompt = f"""
    You are a business validation expert.
    Analyze this business idea and rate it from 1 to 10 based on:
    - Market demand
    - Ease of implementation
    - Profitability
    - Scalability
    Provide the rating and a one-line justification.

    Example output:
    {{
      "score": 8,
      "reason": "Strong demand in AI automation and low entry barrier."
    }}

    Now analyze:
    "{idea}"
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.5,
    )

    text = response.choices[0].message.content.strip()
    return text

import random

def validate_idea(idea):
    score = random.randint(6, 10)
    return score
