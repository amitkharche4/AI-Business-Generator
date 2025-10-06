# generator.py
import os
import json
from datetime import datetime
from OpenAI import OpenAI
from assets import generate_assets
from validate import validate_idea

# ✅ Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_business_ideas():
    """Generate business ideas using GPT."""
    prompt = """
    You are an AI business strategist.
    Generate 3 new, realistic, low-investment business ideas
    that can make around $1,000 per week using AI tools and automation.
    Return results in this format:
    [
      {"idea": "...", "summary": "...", "tools_needed": "..."},
      {"idea": "...", "summary": "...", "tools_needed": "..."},
      {"idea": "...", "summary": "...", "tools_needed": "..."}
    ]
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7,
    )

    text = response.choices[0].message.content
    try:
        ideas = json.loads(text)
    except Exception:
        ideas = [{"idea": f"Idea {i+1}", "summary": text, "tools_needed": "AI tools"} for i in range(3)]
    return ideas


def main():
    print("✅ OpenAI client initialized successfully")
    ideas = generate_business_ideas()

    print("\nGenerated Ideas:")
    for i, idea in enumerate(ideas, 1):
        print(f"{i}. {idea['idea']}")

    results = []
    for idea in ideas:
        score = validate_idea(idea["idea"])
        assets = generate_assets(idea["idea"])
        results.append({
            "idea": idea["idea"],
            "summary": idea["summary"],
            "tools_needed": idea["tools_needed"],
            "validation_score": score,
            "assets": assets,
        })

    output = {
        "generated_at": datetime.utcnow().isoformat(),
        "ideas": results
    }

    with open("latest_ideas.json", "w") as f:
        json.dump(output, f, indent=2)

    print("\n✅ Business ideas and assets generated and saved!")


if __name__ == "__main__":
    main()
