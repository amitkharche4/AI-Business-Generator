
import os
from openai import OpenAI
from assets import generate_assets
from validate import validate_idea

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_business_ideas():
    prompt = """
    Generate 3 online business ideas that can make $1K/week with zero investment.
    For each idea, provide: niche, product/service, monetization method, and target audience.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role":"user","content":prompt}]
    )
    ideas = response.choices[0].message.content
    return ideas

def save_to_file(data, filename="latest_ideas.json"):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    ideas_text = generate_business_ideas()
    ideas_list = [idea.strip() for idea in ideas_text.split("\n") if idea.strip()]

    full_data = []
    for idea in ideas_list:
        score = validate_idea(idea)
        assets = generate_assets(idea)
        full_data.append({
            "idea": idea,
            "market_score": score,
            "assets": assets
        })

    save_to_file(full_data)
    print("Business ideas and assets generated and saved!")
