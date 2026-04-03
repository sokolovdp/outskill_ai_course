import asyncio
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
from typing import AsyncGenerator

import yfinance as yf
from crewai import Agent, Crew, Process, Task
from crewai.llm import LLM
from crewai.tools import tool
from crewai_tools import EXASearchTool
from curl_cffi import requests

from config import EXA_API_KEY, OPENROUTER_API_KEY
from demo.data import ADVANCED_DATA


async def analyze_stock_stream(stock: str, demo: bool) -> AsyncGenerator[dict, None]:
    if demo:
        yield {"type": "phase_update", "phase": "Financial Data", "status": "running", "elapsed": 0}
        await asyncio.sleep(1)
        yield {"type": "phase_update", "phase": "News Research", "status": "running", "elapsed": 0}
        await asyncio.sleep(1.5)
        yield {"type": "phase_update", "phase": "Financial Data", "status": "complete", "elapsed": 2.0}
        await asyncio.sleep(0.5)
        yield {"type": "phase_update", "phase": "News Research", "status": "complete", "elapsed": 2.5}
        await asyncio.sleep(1)

        yield {"type": "phase_update", "phase": "Analysis", "status": "running", "elapsed": 0}
        await asyncio.sleep(3)
        yield {"type": "phase_update", "phase": "Analysis", "status": "complete", "elapsed": 3.0}
        await asyncio.sleep(1)

        yield {"type": "phase_update", "phase": "Recommendation", "status": "running", "elapsed": 0}
        await asyncio.sleep(2)
        yield {"type": "phase_update", "phase": "Recommendation", "status": "complete", "elapsed": 2.0}

        company_info = {k: str(v) for k, v in ADVANCED_DATA["company_info"].items()}
        yield {
            "type": "result",
            "data": {
                "company_info": company_info,
                "financial_analysis": ADVANCED_DATA["financial_analysis"],
                "investment_recommendation": ADVANCED_DATA["investment_recommendation"],
                "recommendation_verdict": "HOLD",
                "timing": {
                    "parallel_time": 2.5,
                    "analysis_time": 3.0,
                    "total_time": 9.5,
                    "time_saved": 2.5,
                },
            },
        }
        return

    os.environ["EXA_API_KEY"] = EXA_API_KEY

    session = requests.Session(impersonate="chrome")

    @tool("Get current stock price")
    def get_current_stock_price(symbol: str) -> str:
        """Get the current stock price for a given symbol."""
        time.sleep(0.5)
        s = yf.Ticker(symbol, session=session)
        price = s.info.get("regularMarketPrice", s.info.get("currentPrice"))
        return f"{price:.2f}" if price else f"Could not fetch current price for {symbol}"

    @tool("Get company info")
    def get_company_info(symbol: str) -> str:
        """Get company information and current financial snapshot for a given stock symbol."""
        info = yf.Ticker(symbol, session=session).info
        if info is None:
            return f"Could not fetch company info for {symbol}"
        cleaned = {
            "Name": info.get("shortName"),
            "Symbol": info.get("symbol"),
            "Current Stock Price": f"{info.get('regularMarketPrice', info.get('currentPrice'))} {info.get('currency', 'USD')}",
            "Market Cap": f"{info.get('marketCap', info.get('enterpriseValue'))} {info.get('currency', 'USD')}",
            "Sector": info.get("sector"),
            "Industry": info.get("industry"),
            "EPS": info.get("trailingEps"),
            "P/E Ratio": info.get("trailingPE"),
            "52 Week Low": info.get("fiftyTwoWeekLow"),
            "52 Week High": info.get("fiftyTwoWeekHigh"),
            "Gross Margins": info.get("grossMargins"),
            "Ebitda Margins": info.get("ebitdaMargins"),
        }
        return json.dumps(cleaned)

    @tool("Get income statements")
    def get_income_statements(symbol: str) -> str:
        """Get income statements for a given stock symbol."""
        s = yf.Ticker(symbol, session=session)
        return s.financials.to_json(orient="index")

    exa_search_tool = EXASearchTool()

    llm = LLM(
        model="openai/gpt-4.1-2025-04-14",
        api_key=OPENROUTER_API_KEY,
        base_url="https://openrouter.ai/api/v1",
    )

    data_explorer = Agent(
        role="Data Researcher",
        goal="Gather and provide financial data and company information about a stock",
        llm=llm,
        verbose=True,
        backstory="You are an expert researcher who can gather detailed information about a company or stock.",
        tools=[get_company_info, get_income_statements],
        cache=True,
        max_iter=5,
        max_execution_time=450,
        max_rpm=12,
        respect_context_window=True,
    )

    news_explorer = Agent(
        role="News and Info Researcher",
        goal="Gather and provide the latest news and information about a company from the internet",
        llm=llm,
        verbose=True,
        backstory="You are an expert researcher, who can gather detailed information about a company.",
        tools=[exa_search_tool],
        cache=True,
        max_iter=5,
        max_execution_time=600,
        max_rpm=15,
        respect_context_window=True,
    )

    analyst = Agent(
        role="Data Analyst",
        goal="Consolidate financial data, stock information, and provide a summary",
        llm=llm,
        verbose=True,
        backstory="You are an expert in analyzing financial data. Use Indian units for numbers (lakh, crore).",
        max_iter=4,
        max_execution_time=300,
        max_rpm=10,
        respect_context_window=True,
    )

    fin_expert = Agent(
        role="Financial Expert",
        goal="Considering financial analysis of a stock, make investment recommendations",
        backstory="You are an expert financial advisor who can provide investment recommendations.",
        llm=llm,
        verbose=True,
        tools=[get_current_stock_price],
        max_iter=5,
        max_execution_time=360,
        max_rpm=8,
        respect_context_window=True,
    )

    get_financials_task = Task(
        description=f"Get financial data like income statements and fundamental ratios for stock: {stock}. Use 2026 as the current year.",
        expected_output="Detailed financial information and key ratios.",
        agent=data_explorer,
    )

    get_news_task = Task(
        description=f"Get latest news and business information about company: {stock}. Use 2026 as the current year.",
        expected_output="Latest news and business information summary.",
        agent=news_explorer,
    )

    analyse_task = Task(
        description="Make thorough analysis based on given financial data and latest news of a stock",
        expected_output="Comprehensive analysis outlining financial health, stock valuation, risks, and news.",
        agent=analyst,
        context=[get_financials_task, get_news_task],
    )

    advise_task = Task(
        description="Make a recommendation about investing in a stock, based on analysis provided and current stock price.",
        expected_output="Recommendation (Buy / Hold / Sell) of a stock backed with reasons.",
        agent=fin_expert,
        context=[analyse_task],
    )

    yield {"type": "phase_update", "phase": "Financial Data", "status": "running", "elapsed": 0}
    yield {"type": "phase_update", "phase": "News Research", "status": "running", "elapsed": 0}

    financial_crew = Crew(agents=[data_explorer], tasks=[get_financials_task], verbose=True)
    news_crew = Crew(agents=[news_explorer], tasks=[get_news_task], verbose=True)

    start = time.time()

    loop = asyncio.get_event_loop()
    with ThreadPoolExecutor(max_workers=2) as executor:
        fin_future = loop.run_in_executor(executor, financial_crew.kickoff, {"stock": stock})
        news_future = loop.run_in_executor(executor, news_crew.kickoff, {"stock": stock})

        fin_result = await fin_future
        fin_time = time.time() - start
        yield {"type": "phase_update", "phase": "Financial Data", "status": "complete", "elapsed": round(fin_time, 1)}

        news_result = await news_future
        news_time = time.time() - start
        yield {"type": "phase_update", "phase": "News Research", "status": "complete", "elapsed": round(news_time, 1)}

    yield {"type": "phase_update", "phase": "Analysis", "status": "running", "elapsed": 0}

    analyse_task_live = Task(
        description="Make thorough analysis based on given financial data and latest news of a stock",
        expected_output="Comprehensive analysis outlining financial health, stock valuation, risks, and news.",
        agent=analyst,
    )

    analysis_crew = Crew(agents=[analyst], tasks=[analyse_task_live], verbose=True)
    context_input = f"Financial Data:\n{fin_result}\n\nNews:\n{news_result}"
    analysis_result = await asyncio.to_thread(analysis_crew.kickoff, {"context": context_input})
    analysis_time = time.time() - start
    yield {"type": "phase_update", "phase": "Analysis", "status": "complete", "elapsed": round(analysis_time - max(fin_time, news_time), 1)}

    yield {"type": "phase_update", "phase": "Recommendation", "status": "running", "elapsed": 0}

    advise_task_live = Task(
        description="Make a recommendation about investing in a stock, based on analysis provided and current stock price.",
        expected_output="Recommendation (Buy / Hold / Sell) backed with reasons.",
        agent=fin_expert,
    )

    rec_crew = Crew(agents=[fin_expert], tasks=[advise_task_live], verbose=True)
    rec_result = await asyncio.to_thread(rec_crew.kickoff, {"analysis": str(analysis_result)})
    total_time = time.time() - start
    yield {"type": "phase_update", "phase": "Recommendation", "status": "complete", "elapsed": round(total_time - analysis_time, 1)}

    rec_text = str(rec_result).lower()
    if "buy" in rec_text:
        verdict = "BUY"
    elif "sell" in rec_text:
        verdict = "SELL"
    else:
        verdict = "HOLD"

    parallel_time = max(fin_time, news_time)
    sequential_time = total_time - parallel_time

    yield {
        "type": "result",
        "data": {
            "company_info": {},
            "financial_analysis": str(analysis_result),
            "investment_recommendation": str(rec_result),
            "recommendation_verdict": verdict,
            "timing": {
                "parallel_time": round(parallel_time, 1),
                "analysis_time": round(sequential_time, 1),
                "total_time": round(total_time, 1),
                "time_saved": round(fin_time + news_time - parallel_time, 1),
            },
        },
    }
