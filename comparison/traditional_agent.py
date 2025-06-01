import random

from google.adk.agents.llm_agent import Agent

# Tools to get a random number
def random_number() -> dict:
    """
    Generate a random number between 1 and 100.
    """    
    return {"number": random.randint(1, 100)}


# Tool to get the weather for a city
def get_weather(city: str) -> dict:
    """
    Get the weather for a given city.
    """
    # Simulating a weather API call
    return {"city": city, "temperature": random.randint(-10, 35), "condition": "Sunny"}


# Define the traditional agent

root_agent = Agent(
    name="traditional_agent",
    model="gemini-2.0-flash",
    instruction="""
    You are a traditional agent that can perform the following tasks:
    1. Generate a random number between 1 and 100.
    2. Get the weather for a given city.
    You can only perform one task at a time.
    """,
    tools=[random_number, get_weather],
)
    