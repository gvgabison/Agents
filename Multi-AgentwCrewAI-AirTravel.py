# ✈Multi-Agent Air Ticket Booking Assistant
!pip install crewai openai

from openai import OpenAI
from crewai import Agent, Task, Crew
import os

# Set OpenAI key and preferred model
os.environ["OPENAI_API_KEY"] = "YourKey"  # Replace with your key
os.environ["MODEL_NAME"] = "gpt-4.1-nano"

client = OpenAI(api_key="YourKey")

# Define Agents
travelbot = Agent(
    name="TravelBot",
    role="Travel Planner",
    goal="Ask the user where they want to go and when",
    backstory="You specialize in understanding travel preferences.",
    verbose=True,
    #llm_config={"model": "gpt-4-1-nano"}
)

searchbot = Agent(
    name="SearchBot",
    role="Flight Finder",
    goal="Search for available flights using mock data",
    backstory="You are an expert in flight APIs and can retrieve airline options quickly.",
    verbose=True,
    #llm_config={"model": "gpt-4-1-nano"}
)

advisorbot = Agent(
    name="AdvisorBot",
    role="Itinerary Advisor",
    goal="Recommend the best flight based on price and convenience",
    backstory="You analyze options and give the most suitable travel recommendation.",
    verbose=True,
    #llm_config={"model": "gpt-4-1-nano"}
)

buyerbot = Agent(
    name="BuyerBot",
    role="Ticket Purchaser",
    goal="Confirm purchase and finalize the ticket",
    backstory="You handle ticket booking securely and efficiently.",
    verbose=True,
    #llm_config={"model": "gpt-4.1-nano"}
)

# Define Tasks
task1 = Task(
    description="Ask the user for their destination and travel date, return as structured input.",
    expected_output="Destination: Paris, Date: 2024-12-25",
    agent=travelbot
)

task2 = Task(
    description="Using the user's destination and date, list 3 mock flight options with airline, time, and price.",
    expected_output="Airline A - 9:00AM - $500; Airline B - 1:00PM - $450; Airline C - 6:00PM - $480",
    agent=searchbot
)

task3 = Task(
    description="Evaluate the 3 flight options and recommend the best one based on value and timing.",
    expected_output="Recommend Airline B at 1:00PM for $600.",
    agent=advisorbot
)

task4 = Task(
    description="Simulate purchasing the recommended flight and provide a ticket confirmation message.",
    expected_output="Ticket purchased successfully for Airline B - 1:00PM - $450. Confirmation #ABC123.",
    agent=buyerbot
)

# Run the Crew
crew = Crew(
    agents=[travelbot, searchbot, advisorbot, buyerbot],
    tasks=[task1, task2, task3, task4],
    verbose=True
)

results = crew.kickoff()
print("Final Output:\n", results)
