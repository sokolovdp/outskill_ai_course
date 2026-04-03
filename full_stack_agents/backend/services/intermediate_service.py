import asyncio
import os
from pathlib import Path
from typing import AsyncGenerator

from crewai import Agent, Crew, Process, Task
from crewai.llm import LLM
from crewai_tools import EXASearchTool, FileReadTool

from config import EXA_API_KEY, OPENROUTER_API_KEY
from demo.data import INTERMEDIATE_REPORTS
from schemas.models import LogFileSchema

DUMMY_LOGS_DIR = Path(__file__).parent.parent / "dummy_logs"


def get_log_files() -> list[LogFileSchema]:
    logs = []
    for f in sorted(DUMMY_LOGS_DIR.iterdir()):
        if f.is_file():
            logs.append(LogFileSchema(name=f.name, content=f.read_text()))
    return logs


async def analyze_logs_stream(log_file: str, demo: bool) -> AsyncGenerator[dict, None]:
    if demo:
        steps = [
            {"step": 1, "agent_name": "Log Analyzer", "status": "running", "output": ""},
            {"step": 1, "agent_name": "Log Analyzer", "status": "complete", "output": INTERMEDIATE_REPORTS["log_analysis"]},
            {"step": 2, "agent_name": "Issue Investigator", "status": "running", "output": ""},
            {"step": 2, "agent_name": "Issue Investigator", "status": "complete", "output": INTERMEDIATE_REPORTS["investigation_report"]},
            {"step": 3, "agent_name": "Solution Specialist", "status": "running", "output": ""},
            {"step": 3, "agent_name": "Solution Specialist", "status": "complete", "output": INTERMEDIATE_REPORTS["solution_plan"]},
        ]
        for event in steps:
            yield event
            await asyncio.sleep(1.5 if event["status"] == "running" else 2)
        return

    os.environ["EXA_API_KEY"] = EXA_API_KEY

    llm = LLM(
        model="openai/gpt-4o",
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )

    log_reader_tool = FileReadTool()
    exa_search_tool = EXASearchTool()

    log_analyzer = Agent(
        role="DevOps Log Analyzer",
        goal="Analyze log files to identify and extract specific issues, errors, and failure patterns",
        llm=llm,
        backstory="You are a senior DevOps engineer with 10 years of experience in analyzing production logs and identifying critical issues.",
        tools=[log_reader_tool],
        verbose=True,
        respect_context_window=True,
        max_iter=3,
        max_execution_time=300,
        max_rpm=10,
    )

    issue_investigator = Agent(
        role="DevOps Issue Investigator",
        goal="Investigate identified issues by searching documentation, forums, and known solutions online",
        llm=llm,
        backstory="You are a DevOps troubleshooting specialist who excels at quickly finding solutions to technical problems.",
        tools=[exa_search_tool],
        verbose=True,
        respect_context_window=True,
        max_iter=5,
        max_execution_time=600,
        max_rpm=15,
    )

    solution_specialist = Agent(
        role="DevOps Solution Specialist",
        goal="Provide clear, actionable solutions with step-by-step instructions based on investigation findings",
        llm=llm,
        backstory="You are a DevOps solutions architect who specializes in creating reliable, step-by-step remediation plans.",
        verbose=True,
        respect_context_window=True,
        max_iter=4,
        max_execution_time=450,
        max_rpm=8,
    )

    log_file_path = str(DUMMY_LOGS_DIR / log_file)

    analyze_logs_task = Task(
        description=f"Analyze the log file at {log_file_path} to identify and extract specific issues.",
        expected_output="A detailed analysis report with primary issue, key error messages, timeline, and root cause.",
        agent=log_analyzer,
    )

    investigate_issue_task = Task(
        description="Based on the log analysis findings, investigate the identified issue online.",
        expected_output="A comprehensive investigation report with similar issues, documentation links, and solutions.",
        agent=issue_investigator,
        context=[analyze_logs_task],
    )

    provide_solution_task = Task(
        description="Based on the log analysis and investigation findings, provide a complete solution.",
        expected_output="A detailed remediation plan with step-by-step commands, verification, and rollback procedures.",
        agent=solution_specialist,
        context=[analyze_logs_task, investigate_issue_task],
    )

    agents = [log_analyzer, issue_investigator, solution_specialist]
    tasks = [analyze_logs_task, investigate_issue_task, provide_solution_task]
    task_names = ["Log Analyzer", "Issue Investigator", "Solution Specialist"]

    crew = Crew(agents=agents, tasks=tasks, process=Process.sequential, verbose=True)

    yield {"step": 1, "agent_name": task_names[0], "status": "running", "output": ""}
    result = await asyncio.to_thread(crew.kickoff)

    for i, task_result in enumerate(result.tasks_output):
        step = i + 1
        yield {"step": step, "agent_name": task_names[i], "status": "complete", "output": str(task_result)}
