# What Can You Build Now?

You've leveled up — you can now orchestrate **multiple agents** working together in a sequential pipeline, pass **context** between tasks so each agent builds on the previous one's work, use **built-in tools** like `FileReadTool` and `EXASearchTool` to give agents real-world capabilities, and fine-tune agent behavior with parameters like `max_iter`, `max_rpm`, and `max_execution_time`.

Here are **10 real-world projects** you can build right now with what you've learned.

---

## 1. SEO Blog Post Pipeline

> Research, write, and optimize a blog post — all in one pipeline.


|                       |                                                                                                                                                                                                                                                                                                                               |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** researches trending keywords and top-ranking articles on a given topic using `EXASearchTool`. **Agent 2** writes a complete blog post using the research context. **Agent 3** optimizes the draft for SEO — restructuring headings, improving keyword density, adding meta descriptions, and scoring readability. |
| **Why it matters**    | Content marketing drives 3x more leads than paid ads. Platforms like Surfer SEO and Jasper AI charge $50-200/month for exactly this pipeline. Companies like HubSpot run this workflow hundreds of times per week.                                                                                                            |
| **Skills you'll use** | 3-agent sequential pipeline, `EXASearchTool` for research, `context` passing between tasks, `output_file` for the final article.                                                                                                                                                                                              |


---

## 2. Customer Support Ticket Resolver

> Read a ticket, find the solution, draft the response.


|                       |                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads the support ticket file using `FileReadTool` and extracts the core issue, affected product, and urgency level. **Agent 2** searches for matching solutions in documentation and community forums using `EXASearchTool`. **Agent 3** drafts a customer-facing response with the fix, relevant links, and a follow-up plan. |
| **Why it matters**    | Zendesk and Intercom handle billions of tickets. The average resolution time is 24 hours — AI-assisted support cuts it to minutes. Freshdesk's AI agent resolution feature directly mirrors this pipeline.                                                                                                                                  |
| **Skills you'll use** | 3-agent pipeline, `FileReadTool` + `EXASearchTool`, context chaining (`context=[ticket_analysis, solution_search]`), structured response output.                                                                                                                                                                                            |


---

## 3. Competitor Intelligence Report

> Monitor competitors and generate strategic briefs automatically.


|                       |                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** searches for the latest news, product launches, and press releases about a competitor using `EXASearchTool`. **Agent 2** analyzes the findings to identify strengths, weaknesses, pricing moves, and market positioning. **Agent 3** produces a strategic recommendations report with actionable takeaways for your team. |
| **Why it matters**    | Competitive intelligence is a $30B+ market. Tools like Crayon and Klue charge enterprise pricing for automated competitor tracking. Every product and strategy team runs some version of this workflow manually.                                                                                                                      |
| **Skills you'll use** | 3-agent sequential pipeline, `EXASearchTool` for real-time data gathering, context chaining, `output_file` for the final report.                                                                                                                                                                                                      |


---

## 4. Academic Literature Reviewer

> Scan the research landscape and find gaps in seconds.


|                       |                                                                                                                                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What it does**      | **Agent 1** searches for recent papers, articles, and publications on a research topic using `EXASearchTool`. **Agent 2** reads through the findings and summarizes key themes, methodologies, and conclusions. **Agent 3** identifies research gaps, contradictions between studies, and suggests future research directions. |
| **Why it matters**    | PhD students and researchers spend weeks on literature reviews. Tools like Elicit and Semantic Scholar are building AI-powered research assistants that follow this exact pattern. The academic AI tools market is growing 35% year-over-year.                                                                                 |
| **Skills you'll use** | 3-agent research pipeline, `EXASearchTool` for paper discovery, context passing for progressive analysis, structured multi-section output.                                                                                                                                                                                     |


---

## 5. Job Application Assistant

> Craft a perfectly tailored cover letter using real company intel.


|                       |                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads a job description file using `FileReadTool` and extracts role requirements, must-haves, and nice-to-haves. **Agent 2** searches for the company's culture, recent news, funding, and values using `EXASearchTool`. **Agent 3** generates a tailored cover letter that maps the candidate's strengths to the JD and weaves in company-specific references. |
| **Why it matters**    | Tailored applications get 50% more interviews than generic ones. Platforms like Teal and Kickresume are adding AI cover letter generation. This is one of the most personally useful agents you can build.                                                                                                                                                                  |
| **Skills you'll use** | 3-agent pipeline, `FileReadTool` + `EXASearchTool` on different agents, dual-context chaining, professional document output.                                                                                                                                                                                                                                                |


---

## 6. Dependency Vulnerability Scanner

> Scan your project's dependencies and get a prioritized security report.


|                       |                                                                                                                                                                                                                                                                                                                                                                                           |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads the project's dependency file (`requirements.txt`, `package.json`) using `FileReadTool` and extracts all packages with versions. **Agent 2** searches for known CVEs and security advisories for each dependency using `EXASearchTool`. **Agent 3** produces a prioritized vulnerability report with severity levels, affected versions, and recommended upgrade paths. |
| **Why it matters**    | Snyk and Dependabot are billion-dollar tools built on this workflow. The Log4Shell vulnerability alone cost companies an estimated $10B. Security scanning is a non-negotiable part of modern DevOps — exactly the domain you built your workshop project in.                                                                                                                             |
| **Skills you'll use** | 3-agent pipeline, `FileReadTool` for code artifacts, `EXASearchTool` for vulnerability databases, context chaining, structured priority-ranked output.                                                                                                                                                                                                                                    |


---

## 7. Product Launch Checklist Generator

> Go from product spec to launch plan automatically.


|                       |                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads the product specification document using `FileReadTool` and extracts features, target audience, and launch timeline. **Agent 2** researches competitor launches and industry best practices using `EXASearchTool`. **Agent 3** produces a comprehensive go-to-market checklist with tasks, owners, deadlines, and channel strategy. |
| **Why it matters**    | Product launches involve 50+ tasks across marketing, engineering, sales, and support. Tools like Asana and Monday.com offer launch templates, but AI-generated checklists tailored to your specific product are far more valuable.                                                                                                                    |
| **Skills you'll use** | 3-agent pipeline, `FileReadTool` + `EXASearchTool`, context chaining, structured checklist output with `output_file`.                                                                                                                                                                                                                                 |


---

## 8. Podcast Show Notes Generator

> Turn a raw transcript into polished, publish-ready show notes.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                     |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads the podcast transcript using `FileReadTool` and extracts key topics, timestamps, guest quotes, and resources mentioned. **Agent 2** takes the extracted topics and searches for relevant links, articles, and references using `EXASearchTool`. **Agent 3** generates formatted show notes with a summary, timestamped sections, guest bio, resource links, and a call-to-action. |
| **Why it matters**    | There are 4M+ active podcasts. Show notes are critical for SEO and discoverability but take 1-2 hours per episode to write manually. Podcast platforms like Transistor and Castmagic are investing heavily in AI-generated show notes.                                                                                                                                                              |
| **Skills you'll use** | 3-agent pipeline, `FileReadTool` for transcript, `EXASearchTool` for link enrichment, progressive context building, formatted markdown output.                                                                                                                                                                                                                                                      |


---

## 9. Real Estate Listing Analyzer

> Get an investment-grade analysis of any property listing.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads the property listing data file using `FileReadTool` and extracts price, location, size, amenities, and listing history. **Agent 2** searches for comparable sales, neighborhood trends, and market conditions using `EXASearchTool`. **Agent 3** produces an investment analysis with price-per-sqft comparison, rental yield estimate, risk factors, and a `Buy` / `Hold` / `Skip` recommendation. |
| **Why it matters**    | Zillow's Zestimate and Redfin's pricing models are AI-powered property analysis at scale. Real estate investors make decisions based on exactly this kind of comparative analysis — but doing it manually takes hours per listing.                                                                                                                                                                                    |
| **Skills you'll use** | 3-agent pipeline, `FileReadTool` + `EXASearchTool`, multi-source context chaining, structured analytical output with recommendation.                                                                                                                                                                                                                                                                                  |


---

## 10. Incident Post-Mortem Generator

> Go from raw logs to a complete post-mortem document — automatically.


|                       |                                                                                                                                                                                                                                                                                                                                                                                                                             |
| --------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads the incident log file using `FileReadTool` and identifies the failure timeline, error patterns, and root cause indicators. **Agent 2** searches for best-practice post-mortem templates and similar incidents at other companies using `EXASearchTool`. **Agent 3** produces a complete post-mortem document with incident summary, timeline, root cause analysis, action items, and prevention measures. |
| **Why it matters**    | Google, Meta, and every serious engineering org runs post-mortems after incidents. PagerDuty and FireHydrant sell post-mortem tooling. Writing them is tedious and often delayed — this agent generates a solid first draft immediately after an incident. This is a direct extension of the DevOps project you built in the workshop.                                                                                      |
| **Skills you'll use** | 3-agent pipeline, `FileReadTool` + `EXASearchTool`, full context chain (`context=[log_analysis, investigation]`), comprehensive document output with `output_file`.                                                                                                                                                                                                                                                         |


---

> **Tip**: Every project above follows the same architecture you built in the workshop — a sequential multi-agent pipeline where each agent's output feeds into the next via `context`. The power comes from combining the right **tools** with the right **agents** and letting context flow downstream. Pick any project, swap out the agent roles and task descriptions, and you have a production-ready pipeline.

