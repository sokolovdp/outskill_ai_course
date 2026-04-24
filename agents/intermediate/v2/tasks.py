import os

from crewai import Task
from crewai.tasks.task_output import TaskOutput
from pydantic import BaseModel, Field

from agents import issue_investigator, log_analyzer, solution_specialist

os.makedirs("task_outputs", exist_ok=True)


# ──────────────────────────────────────────────────────────
# Pydantic models for structured output
# ──────────────────────────────────────────────────────────

class ErrorEntry(BaseModel):
    message: str = Field(description="The error message text")
    severity: str = Field(description="ERROR, CRITICAL, or WARNING")
    timestamp: str = Field(description="When the error occurred")


class LogAnalysisReport(BaseModel):
    primary_issue: str = Field(description="One-line description of the main issue")
    root_cause: str = Field(description="Root cause analysis based on log evidence")
    errors: list[ErrorEntry] = Field(description="All errors found in the log")
    affected_components: list[str] = Field(description="System components affected")
    timeline: list[str] = Field(description="Sequence of events leading to failure")


class InvestigationReport(BaseModel):
    similar_issues: list[str] = Field(description="Similar issues found online with references")
    official_docs: list[str] = Field(description="Official documentation links")
    common_causes: list[str] = Field(description="Common causes ranked by likelihood")
    verified_solutions: list[str] = Field(description="Community-verified solutions")
    best_practices: list[str] = Field(description="Best practices to prevent recurrence")


class SolutionStep(BaseModel):
    step_number: int = Field(description="Step number in the remediation plan")
    action: str = Field(description="What to do")
    command: str = Field(description="Specific command to run, if applicable")


class SolutionPlan(BaseModel):
    primary_solution: list[SolutionStep] = Field(description="Step-by-step remediation plan")
    verification_steps: list[str] = Field(description="How to verify the fix worked")
    prevention_measures: list[str] = Field(description="How to prevent this in the future")
    rollback_plan: str = Field(description="What to do if the fix fails")
    doc_references: list[str] = Field(description="Links to official documentation")


# ──────────────────────────────────────────────────────────
# Guardrails
# ──────────────────────────────────────────────────────────

def validate_log_analysis(result: TaskOutput) -> tuple[bool, any]:
    """Code guardrail: ensures the analysis found actual errors and a root cause."""
    if not result.pydantic:
        return (False, "Output must be a structured LogAnalysisReport")
    report = result.pydantic
    if not report.errors:
        return (False, "Analysis must identify at least one error from the logs")
    if not report.root_cause:
        return (False, "Root cause analysis is required")
    return (True, report)


# ──────────────────────────────────────────────────────────
# Tasks
# ──────────────────────────────────────────────────────────

# Task 1: Structured output + code guardrail
analyze_logs_task = Task(
    description="""Analyze the log file at {log_file_path} to identify and extract specific issues.
    
    Your analysis should:
    1. Read through the entire log file carefully
    2. Identify all ERROR, CRITICAL, and WARNING messages
    3. Extract the main issue or failure pattern
    4. Determine the timeline of events leading to the failure
    5. Identify the root cause from the log entries
    
    Focus on finding the primary issue that needs to be resolved.""",
    expected_output="A structured log analysis report with errors, root cause, and timeline",
    output_pydantic=LogAnalysisReport,
    guardrail=validate_log_analysis,
    agent=log_analyzer,
    output_file="task_outputs/log_analysis.md",
)

# Task 2: Structured output
investigate_issue_task = Task(
    description="""Based on the log analysis findings, investigate the identified issue online.
    
    Your investigation should:
    1. Search for similar errors and issues in documentation and forums
    2. Find official documentation related to the error
    3. Look for community solutions and best practices
    4. Identify common causes and scenarios for this type of issue
    5. Gather information about proven fixes and workarounds
    
    Focus on finding reliable, well-documented solutions.""",
    expected_output="A structured investigation report with solutions and references",
    output_pydantic=InvestigationReport,
    agent=issue_investigator,
    context=[analyze_logs_task],
    output_file="task_outputs/investigation_report.md",
)

# Task 3: No-code guardrail
provide_solution_task = Task(
    description="""Based on the log analysis and investigation findings, provide a complete solution.
    
    Your solution should:
    1. Create a step-by-step remediation plan with specific commands
    2. Provide verification steps to confirm the fix
    3. Suggest monitoring and prevention measures
    4. Include rollback procedures if needed
    5. Reference official documentation
    
    Ensure all commands are copy-pasteable and all solutions are practical.""",
    expected_output="A structured remediation plan with commands, verification, and prevention",
    output_pydantic=SolutionPlan,
    guardrail="The solution must include at least 3 specific, copy-pasteable commands. "
    "Reject if it only contains general advice without concrete commands.",
    agent=solution_specialist,
    context=[analyze_logs_task, investigate_issue_task],
    output_file="task_outputs/solution_plan.md",
)
