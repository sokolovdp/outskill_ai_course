# What Can You Build Now?

You've reached the advanced tier — you can now split work across **multiple crews**, run independent crews in **parallel** with `ThreadPoolExecutor`, build **custom tools** with the `@tool` decorator that connect to any API, design **multi-phase pipelines** (parallel data gathering → sequential analysis), and expose your agent system as a **REST API** with FastAPI.

Here are **10 real-world projects** you can build right now with what you've learned.

---

## 1. AI-Powered Hiring Pipeline

> Source candidates, score them, and generate interview kits — all in parallel.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Crew 1** (parallel): uses a custom tool to fetch candidate profiles from a jobs API + uses `EXASearchTool` to gather company Glassdoor reviews and culture data. **Crew 2** (sequential): an analyst agent scores candidates against the job description, then an HR specialist generates tailored interview kits with role-specific questions. Exposed via a FastAPI endpoint that takes a JD and returns ranked candidates. |
| **Why it matters**    | LinkedIn Recruiter and HireVue process millions of candidates with AI scoring. Enterprise hiring pipelines cost $4,000+ per hire — AI-assisted screening can cut that by 60%. This project demonstrates the full production pattern: parallel data ingestion, sequential analysis, and API delivery.                                                                                                                            |
| **Skills you'll use** | Multiple crews, `ThreadPoolExecutor` for parallel execution, custom `@tool` for job board API, FastAPI server, multi-phase pipeline.                                                                                                                                                                                                                                                                                            |


---

## 2. Multi-Source News Aggregator & Fact Checker

> Aggregate news from multiple sources in parallel, then cross-reference and fact-check.


|                       |                                                                                                                                                                                                                                                                                                                                                                                         |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Crew 1** (parallel): a news agent fetches articles via a custom RSS/news API tool + a social media agent gathers public sentiment and trending discussions using `EXASearchTool`. **Crew 2** (sequential): a fact-checker agent cross-references claims across the collected sources, then a reporter agent produces a fact-checked news brief with confidence scores for each claim. |
| **Why it matters**    | Misinformation costs the global economy $78B annually. Tools like NewsGuard and Google Fact Check Explorer are building exactly this — multi-source verification pipelines. News organizations like Reuters and AP are investing in AI-assisted fact-checking at scale.                                                                                                                 |
| **Skills you'll use** | Multiple crews, parallel execution, custom `@tool` for RSS/news APIs, context from multiple upstream tasks, structured output with confidence scoring.                                                                                                                                                                                                                                  |


---

## 3. E-Commerce Price Intelligence Agent

> Monitor competitor prices and generate pricing strategy recommendations in real-time.


|                       |                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Crew 1** (parallel): a price tracker agent fetches competitor prices using a custom scraping tool + a reviews agent gathers product review sentiment using `EXASearchTool`. **Crew 2** (sequential): an analyst agent compares pricing across competitors and identifies patterns, then a strategist agent generates dynamic pricing recommendations with projected revenue impact. |
| **Why it matters**    | Amazon changes prices 2.5 million times per day. Pricing intelligence tools like Prisync and Competera charge $500-5,000/month. E-commerce companies that use dynamic pricing see 5-10% revenue increases. The parallel scraping pattern mirrors exactly how these tools work at scale.                                                                                               |
| **Skills you'll use** | Multiple crews, `ThreadPoolExecutor`, custom `@tool` for price scraping, parallel data collection, sequential analysis with recommendations.                                                                                                                                                                                                                                          |


---

## 4. Real-Time Crypto Portfolio Advisor

> Fetch live market data and news in parallel, then generate rebalancing recommendations.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Crew 1** (parallel): a data agent fetches live prices, 24h volume, and market cap via a custom CoinGecko API tool + a news agent gathers crypto-specific news and regulatory updates using `EXASearchTool`. **Crew 2** (sequential): an analyst consolidates all data and evaluates portfolio allocation, then a financial advisor generates rebalancing recommendations with risk-adjusted returns. Output saved to a portfolio report file. |
| **Why it matters**    | The crypto market runs 24/7 with extreme volatility. Portfolio trackers like CoinStats and CoinGecko serve 10M+ users. This is a direct extension of the stock advisor you built in the workshop — same architecture, different asset class, equally valuable.                                                                                                                                                                                  |
| **Skills you'll use** | Multiple crews, parallel execution, custom `@tool` with CoinGecko API (mirrors the yfinance pattern), multi-phase pipeline, `output_file`, `argparse` for CLI.                                                                                                                                                                                                                                                                                  |


---

## 5. GitHub Repository Health Analyzer

> Audit any open-source repo for quality, security, and maintainability — in one command.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Crew 1** (parallel): a stats agent fetches repo metrics (stars, issues, PR velocity, contributor count) via a custom GitHub API tool + a security agent searches for known vulnerabilities and CVEs using `EXASearchTool`. **Crew 2** (sequential): an analyst scores the repo across dimensions (activity, community, security, documentation), then an advisor generates a health report card with an overall grade and specific improvement recommendations. |
| **Why it matters**    | FOSS risk management is critical — companies like Snyk, Socket, and GitHub's own Dependabot analyze repo health to flag supply chain risks. Engineering teams evaluate dozens of open-source dependencies before adoption. This agent automates that due diligence.                                                                                                                                                                                               |
| **Skills you'll use** | Multiple crews, `ThreadPoolExecutor`, custom `@tool` with GitHub REST API, parallel data gathering, scoring system output, `output_file`.                                                                                                                                                                                                                                                                                                                         |


---

## 6. Travel Itinerary Planner with Live Data

> Build a day-by-day travel plan powered by real-time flight, weather, and event data.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What it does**      | **Crew 1** (parallel): a flights agent fetches prices using a custom API tool + a weather agent gets forecasts via a weather API tool + an events agent searches for local events and activities using `EXASearchTool`. **Crew 2** (sequential): a planner agent builds an optimized day-by-day itinerary considering weather and events, then a budget agent generates a complete cost breakdown with alternatives for different budgets. |
| **Why it matters**    | The travel planning AI market is projected to hit $1.4B by 2027. CrewAI's own official examples include a trip planner — it's one of the most popular demo projects because it perfectly showcases parallel data gathering from diverse APIs feeding into sequential planning.                                                                                                                                                             |
| **Skills you'll use** | 3+ crews, parallel execution with 3 concurrent crews, multiple custom `@tool` decorators, multi-phase pipeline, structured itinerary output.                                                                                                                                                                                                                                                                                               |


---

## 7. AI Sales Intelligence Platform

> Enrich leads and generate personalized pitch decks — exposed as an API.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What it does**      | **Crew 1** (parallel): an enrichment agent fetches company data (size, revenue, tech stack) via a custom company data API tool + a news agent gathers recent press, funding rounds, and leadership changes using `EXASearchTool`. **Crew 2** (sequential): a scoring agent evaluates lead quality based on ICP fit, then a sales strategist generates a personalized pitch deck outline with talking points tailored to the prospect's recent activity. Exposed via FastAPI for CRM integration. |
| **Why it matters**    | Sales intelligence is a $5B market led by ZoomInfo, Apollo, and Clearbit. Enterprise sales teams pay $10K+/year per seat for enriched lead data. This project combines data enrichment, scoring, and content generation — the three pillars of modern sales tech.                                                                                                                                                                                                                                |
| **Skills you'll use** | Multiple crews, `ThreadPoolExecutor`, custom `@tool` for company APIs, FastAPI REST endpoints, parallel enrichment, sequential analysis.                                                                                                                                                                                                                                                                                                                                                         |


---

## 8. Open Source License Compliance Auditor

> Scan a project's dependency tree and flag license conflicts before they become legal problems.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Crew 1** (parallel): a parser agent reads dependency files and extracts the full dependency tree using a custom tool + a license agent fetches license metadata from npm/PyPI registries via another custom tool. **Crew 2** (sequential): a compliance analyst identifies license incompatibilities (e.g., GPL in a proprietary project), then a legal advisor produces a compliance report with risk levels, flagged packages, and recommended alternatives. |
| **Why it matters**    | License violations have led to lawsuits costing millions (Oracle v. Google, Cisco v. FSF). Tools like FOSSA and WhiteSource (now Mend) charge enterprise pricing for license compliance. Every company shipping software needs this audit — most do it manually or not at all.                                                                                                                                                                                   |
| **Skills you'll use** | Multiple crews, parallel execution, two custom `@tool` functions (dependency parser + registry API), multi-phase analysis, risk-ranked output.                                                                                                                                                                                                                                                                                                                   |


---

## 9. Content Repurposing Engine

> Turn one piece of content into five — across platforms, in parallel.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Crew 1** (parallel): a transcription agent processes a video/podcast transcript using a custom parser tool + a trends agent researches what's currently trending in the niche using `EXASearchTool`. **Crew 2** (sequential): a content strategist identifies the top 3 angles from the source material, then a writer agent generates five outputs — a blog post, a Twitter/X thread, a LinkedIn post, an email newsletter snippet, and a short-form video script. Each output saved to a separate `output_file`. |
| **Why it matters**    | Content repurposing is how creators like Ali Abdaal and companies like HubSpot 10x their output. Repurpose.io and Opus Clip are venture-backed tools doing exactly this. One podcast episode can generate a week of content — if you have the pipeline.                                                                                                                                                                                                                                                              |
| **Skills you'll use** | Multiple crews, `ThreadPoolExecutor`, custom `@tool` for transcript parsing, parallel research, multiple `output_file` targets, multi-format content generation.                                                                                                                                                                                                                                                                                                                                                     |


---

## 10. **Smart Home Energy Optimizer**

> Fetch real-time energy rates and weather, then generate an optimization schedule.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Crew 1** (parallel): an energy agent fetches current and forecasted electricity rates using a custom utility API tool + a weather agent retrieves temperature and solar radiation forecasts via a weather API tool. **Crew 2** (sequential): an analyst agent correlates energy rates with weather patterns and historical usage, then an optimizer agent generates a daily appliance schedule (when to run the dishwasher, charge EV, adjust thermostat) with estimated monthly savings. |
| **Why it matters**    | Smart home energy management is a $15B market. Products like Sense, OhmConnect, and Google Nest optimize energy usage based on rate data and weather. With time-of-use pricing becoming standard, homeowners can save 20-30% on electricity bills with smart scheduling.                                                                                                                                                                                                                    |
| **Skills you'll use** | Multiple crews, parallel execution, multiple custom `@tool` functions (energy API + weather API), multi-phase pipeline, actionable schedule output with savings projections.                                                                                                                                                                                                                                                                                                                |


---

> **Tip**: Every project above follows the same architecture you built in the workshop — parallel data gathering with `ThreadPoolExecutor` across independent crews, followed by sequential analysis in a dependent crew. The power comes from building **custom tools** that connect your agents to any API or data source. Swap in different APIs, change the agent roles, and you can build an intelligent pipeline for virtually any domain.

