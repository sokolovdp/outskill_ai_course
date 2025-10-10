from crewai import Crew, Process

from agents import content_explorer, script_writer
from tasks import create_a_script, get_details

# Define the crew with agents and tasks in sequential process
crew = Crew(
    agents=[content_explorer, script_writer],
    tasks=[get_details, create_a_script],
    verbose=True,
    Process=Process.sequential,
)

# Run the crew with a specific stock
result = crew.kickoff(inputs={"topic": "Will OpenAI release AGI in 2026?"})

# print("Response:", result)
