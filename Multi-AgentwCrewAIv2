# 📦 Install required libraries
!pip install crewai openai

# 🔑 Initialize the OpenAI SDK
from openai import OpenAI
client = OpenAI(api_key="yourkeyhere")  # Replace with your actual OpenAI key

# 🧠 Define Agents with backstory and goals
from crewai import Agent

planner = Agent(
    name="Planner",
    role="Task Planner",
    goal="Break down complex queries into subtasks",
    backstory="You are an experienced project planner helping an AI writing team be more efficient.",
    verbose=True
)

researcher = Agent(
    name="Researcher",
    role="Research Analyst",
    goal="Search and summarize relevant information",
    backstory="You are a skilled analyst who gathers trustworthy and useful knowledge.",
    verbose=True
)

writer = Agent(
    name="Writer",
    role="Content Writer",
    goal="Write a final article from research notes",
    backstory="You specialize in writing clear, concise articles from structured research.",
    verbose=True
)

# 📋 Define tasks and assign to agents
from crewai import Task

task1 = Task(
    description="Create subtasks for a blog about AI in finance",
    expected_output="List of subtasks",
    agent=planner
)

task2 = Task(
    description="Research each subtask and summarize findings",
    expected_output="Summary notes",
    agent=researcher
)

task3 = Task(
    description="Write a 300-word article using the research",
    expected_output="Completed blog post",
    agent=writer
)

# 🧩 Assemble the Crew and run
from crewai import Crew
import os

# Set API key via environment (needed by LiteLLM)
os.environ["OPENAI_API_KEY"] = "yourkeyhere"  # Replace again if needed

crew = Crew(
    agents=[planner, researcher, writer],
    tasks=[task1, task2, task3],
    verbose=True
)

# 🚀 Launch the workflow
results = crew.kickoff()
print("Final Output:\n", results)
