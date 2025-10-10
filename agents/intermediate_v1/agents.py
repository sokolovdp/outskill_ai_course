import os

from crewai import Agent
from crewai.llm import LLM
from dotenv import load_dotenv

load_dotenv()

from tools import exa_search_tool

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
llm = LLM(model="gpt-4o", temperature=0.9)

## Agent designed to gather information about a topic from internet.
content_explorer = Agent(
    role="content explorer",
    goal="Gather and provide latest information about the topic from internet",
    llm=llm,
    backstory=(
        "You are an expert researcher, who can gather detailed information about a topic.\
                  Gather at least 10 information."
    ),
    tools=[exa_search_tool],
    cache=True,
    max_iter=5,
)

script_writer = Agent(
    role="Script Writer",
    goal="With the details given to you create an interesting conversational script out of it",
    llm=llm,
    backstory=(
        "You are an expert in literature. \
                  You are very good in creating conversations with the given chain of information. \
                  Tell as a script in 200 words."
    ),
)

# os.environ['OTEL_SDK_DISABLED'] = "True"
