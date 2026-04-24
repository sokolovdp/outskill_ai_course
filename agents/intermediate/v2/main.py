import os

from crewai import Crew, Process
from tasks import analyze_logs_task, investigate_issue_task, provide_solution_task

from agents import issue_investigator, log_analyzer, solution_specialist

# Enhanced DevOps crew with all v2 features:
#   - memory=True:  agents remember across runs
#   - Structured output, guardrails, human input are configured in tasks.py
devops_crew = Crew(
    agents=[log_analyzer, issue_investigator, solution_specialist],
    tasks=[analyze_logs_task, investigate_issue_task, provide_solution_task],
    verbose=True,
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=30,
)

if __name__ == "__main__":
    print("=" * 60)
    print("DevOps Issue Analysis v2")
    print("Features: Structured Output | Guardrails | Human Input | Memory")
    print("=" * 60)

    # Scenario 1: Kubernetes deployment error
    print("\nScenario 1: Kubernetes Deployment Analysis")
    print("-" * 40)
    result1 = devops_crew.kickoff(
        inputs={"log_file_path": "../../dummy_logs/kubernetes_deployment_error.log"}
    )

    # Print structured results from the analysis
    if result1.pydantic:
        plan = result1.pydantic
        print(f"\nSolution steps: {len(plan.primary_solution)}")
        for step in plan.primary_solution:
            print(f"  {step.step_number}. {step.action}")
            if step.command:
                print(f"     $ {step.command}")

    # Scenario 2: Database connection error (uncomment to run)
    # The agent will recall patterns from Scenario 1 thanks to memory.
    # print("\nScenario 2: Database Connection Analysis")
    # print("-" * 40)
    # result2 = devops_crew.kickoff(
    #     inputs={"log_file_path": "../../dummy_logs/database_connection_error.log"}
    # )

    print("\nAnalysis completed!")
    print("To inspect stored memories, run:")
    print("  python ../../crewai_memory_explorer.py crewai_memory")
