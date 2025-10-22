from dotenv import load_dotenv
import os
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.exa import ExaTools

load_dotenv()

def create_shopping_agent():
    if not os.getenv("GOOGLE_API_KEY"):
        raise ValueError("Missing GOOGLE_API_KEY in .env")
    if not os.getenv("EXA_API_KEY"):
        raise ValueError("Missing EXA_API_KEY in .env")

    return Agent(
        name="Shopping Partner",
        model=Gemini(id="gemini-2.5-pro"),
        instructions=[
            "You are a shopping assistant AI that finds authentic, in-stock products.",
            "Only recommend from Amazon, Flipkart, Myntra, Meesho, Nike, or Google Shopping.",
            "Always include name, brand, price, features, and link.",
            "Avoid fake or unavailable products.",
            "Format output cleanly with bullet points or tables.",
        ],
        tools=[ExaTools()],
    )
