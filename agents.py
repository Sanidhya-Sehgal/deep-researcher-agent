import os
from dotenv import load_dotenv
import requests
import ollama
from groq import Groq

load_dotenv()


# =========================
# 🔥 LLM HYBRID FUNCTION
# =========================
def generate_response(prompt: str) -> str:
    use_local = os.getenv("USE_LOCAL", "true").lower() == "true"

    if use_local:
        # 🟢 Use Ollama (Local)
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}],
        )
        return response["message"]["content"]

    else:
        # 🔵 Use Groq (Cloud)
        client = Groq(api_key=os.getenv("GROQ_API_KEY"))

        completion = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
        )
        return completion.choices[0].message.content


# =========================
# 🔍 SCRAPER (WIKIPEDIA)
# =========================
def scrape_data(query: str) -> str:
    # Improve short/ambiguous queries
    if len(query.split()) <= 2:
        query = query + " computer science"

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query.replace(' ', '_')}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data.get("extract", "No data found")

        return "No data found"

    except Exception as e:
        print(f"Scraping error: {e}")
        return "Error fetching data"


# =========================
# 🧠 MAIN WORKFLOW
# =========================
class DeepResearcherAgent:
    """
    Hybrid AI Research Agent:
    - Scrapes data (Wikipedia)
    - Uses LLM (Ollama/Groq)
    - Generates structured report
    """

    def run(self, topic: str) -> str:
        print(f"Running research for topic: {topic}")

        # Step 1: Scrape data
        raw_data = scrape_data(topic)

        # Fallback if no data found
        if raw_data == "No data found" or raw_data.strip() == "":
            raw_data = generate_response(
                f"Explain {topic} in detail in computer science context"
            )

        # Step 2 + 3: Combined Analysis + Report
        final_prompt = f"""
You are an expert technical researcher and writer.

Topic: {topic}

Data:
{raw_data}

Instructions:
- If the data is limited or missing, use your own knowledge
- Explain the topic clearly
- Include key concepts
- Include real-world applications

Create a detailed report with:
- Introduction
- Key Concepts
- Applications
- Conclusion
"""

        final_report = generate_response(final_prompt)

        print("Report generated")

        return final_report


# =========================
# 🚀 RUN FUNCTION
# =========================
def run_research(query: str) -> str:
    agent = DeepResearcherAgent()
    return agent.run(query)


# =========================
# 🧪 TEST
# =========================
if __name__ == "__main__":
    topic = "Artificial Intelligence"
    response = run_research(topic)
    print(response)