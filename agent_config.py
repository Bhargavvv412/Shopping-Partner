# agent_config.py
from agno.agent import Agent
from agno.models.google.gemini import Gemini
from agno.tools.exa import ExaTools
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

def create_shopping_agent():
    # Optional: verify keys
    google_key = os.getenv("GOOGLE_API_KEY")
    exa_key = os.getenv("EXA_API_KEY")

    if not google_key or not exa_key:
        raise ValueError("❌ API keys missing. Please set GOOGLE_API_KEY and EXA_API_KEY in .env")

    return Agent(
        name="Shopping Partner",
        model=Gemini(id="gemini-2.5-pro"),
        instructions=[
            "You are a shopping assistant AI that finds authentic, in-stock products.",
            "Recommend only from Amazon, Flipkart, Myntra, Nike, Meesho, or Google Shopping.",
            "Provide name, brand, price, color, and features clearly.",
        ],
        tools=[ExaTools()],
    )

if __name__ == "__main__":
    agent = create_shopping_agent()
    agent.print_response("Find black running shoes under ₹10,000 for long-distance running.")
