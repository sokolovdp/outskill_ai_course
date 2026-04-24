import asyncio
import time

from crewai import Crew, Process
from crewai.flow.flow import Flow, listen, router, start
from pydantic import BaseModel

from agents import (
    analyst,
    data_explorer,
    entry_strategist,
    exit_planner,
    fin_expert,
    hold_monitor,
    news_info_explorer,
)
from tasks import (
    InvestmentRecommendation,
    advise,
    analyse,
    entry_strategy_task,
    exit_plan_task,
    get_company_financials,
    get_company_news,
    monitoring_plan_task,
    validate_recommendation,
)

financial_crew = Crew(
    agents=[data_explorer],
    tasks=[get_company_financials],
    verbose=True,
    process=Process.sequential,
    cache=True,
    max_rpm=15,
)

news_crew = Crew(
    agents=[news_info_explorer],
    tasks=[get_company_news],
    verbose=True,
    process=Process.sequential,
    cache=True,
    max_rpm=15,
)

analysis_crew = Crew(
    agents=[analyst, fin_expert],
    tasks=[analyse, advise],
    verbose=True,
    process=Process.sequential,
    cache=True,
    max_rpm=15,
)

entry_crew = Crew(
    agents=[entry_strategist],
    tasks=[entry_strategy_task],
    verbose=True,
    process=Process.sequential,
    cache=True,
    max_rpm=10,
)

exit_crew = Crew(
    agents=[exit_planner],
    tasks=[exit_plan_task],
    verbose=True,
    process=Process.sequential,
    cache=True,
    max_rpm=10,
)

hold_crew = Crew(
    agents=[hold_monitor],
    tasks=[monitoring_plan_task],
    verbose=True,
    process=Process.sequential,
    cache=True,
    max_rpm=10,
)


class AnalysisState(BaseModel):
    stock: str = ""
    action: str = ""
    recommendation_raw: str = ""
    final_report: str = ""


class InvestmentFlow(Flow[AnalysisState]):

    @start()
    def analyze_stock(self):
        result = analysis_crew.kickoff(inputs={"stock": self.state.stock})
        self.state.action = result.pydantic.action if result.pydantic else "HOLD"
        self.state.recommendation_raw = result.raw
        return self.state.action

    @router(analyze_stock)
    def pick_next_step(self):
        if self.state.action == "BUY":
            return "buy_path"
        elif self.state.action == "SELL":
            return "sell_path"
        return "hold_path"

    @listen("buy_path")
    def generate_entry_strategy(self):
        result = entry_crew.kickoff(inputs={"stock": self.state.stock})
        self.state.final_report = result.raw

    @listen("sell_path")
    def generate_exit_plan(self):
        result = exit_crew.kickoff(inputs={"stock": self.state.stock})
        self.state.final_report = result.raw

    @listen("hold_path")
    def generate_monitoring_plan(self):
        result = hold_crew.kickoff(inputs={"stock": self.state.stock})
        self.state.final_report = result.raw


async def analyze_watchlist(stocks: list[str]):
    tasks = [analysis_crew.kickoff_async(inputs={"stock": s}) for s in stocks]
    results = await asyncio.gather(*tasks)
    return dict(zip(stocks, results))


if __name__ == "__main__":
    stock = "AAPL"
    print(f"Running Investment Flow for {stock}...")
    start_time = time.time()

    flow = InvestmentFlow()
    flow.kickoff(inputs={"stock": stock})

    elapsed = time.time() - start_time
    print(f"\nAction: {flow.state.action}")
    print(f"Time: {elapsed:.2f}s")
    print(f"\nFinal Report:\n{flow.state.final_report[:500]}")
