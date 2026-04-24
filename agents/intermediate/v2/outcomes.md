# What Can You Build Now?

You now have **production-grade** agent capabilities: **structured output** that gives you typed Python objects instead of raw text, **guardrails** that make agents self-correct when output quality is insufficient, and **memory** so agents learn across runs.

Here are **10 real-world projects** you can build with what you've learned.

---

## 1. Legal Contract Reviewer

> Extract structured clauses, flag risky terms, and validate with guardrails.


|                       |                                                                                                                                                                                                                                                                                                                                                |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads a contract and extracts key clauses into a structured `ContractAnalysis` model (parties, terms, obligations, expiry dates). **Agent 2** flags risky clauses with a guardrail ensuring every flagged clause has a severity level and recommendation. **Agent 3** drafts a review summary for lawyer review. |
| **Why it matters**    | Legal review costs $300-500/hour. Tools like Kira Systems and LawGeex automate exactly this. The structured output means you can programmatically track clause types across hundreds of contracts.                                                                                                                            |
| **Skills you'll use** | `output_pydantic` for contract structure, code guardrail to validate clause extraction, `memory=True` to learn patterns across contracts.                                                                                                                                                                                    |


---

## 2. Medical Symptom Triage System

> Structured symptom extraction, safety guardrails, cross-case memory.


|                       |                                                                                                                                                                                                                                                                                                                                              |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** extracts symptoms from a patient description into a structured `SymptomReport` (symptoms, severity, duration). A code guardrail rejects analysis that doesn't assign severity levels. **Agent 2** suggests possible conditions. **Agent 3** drafts triage recommendations for human review. |
| **Why it matters**    | Medical AI must be reliable. The guardrail prevents incomplete analysis from reaching patients. Ada Health and Babylon Health follow this exact pattern.                                                                                                                          |
| **Skills you'll use** | `output_pydantic` for symptom structure, code guardrail for completeness validation, `memory=True` to recall similar cases.                                                                                                                                                                     |


---

## 3. E-Commerce Product Listing Optimizer

> Structured product data, quality guardrails on descriptions, iterative refinement.


|                       |                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads raw product data and outputs a structured `ProductListing` (title, bullet points, keywords, category). **Agent 2** rewrites the description for SEO with a no-code guardrail: "Must include at least 5 keyword phrases and a clear call-to-action." **Agent 3** generates A/B test variants. |
| **Why it matters**    | Amazon sellers optimize thousands of listings. Tools like Helium 10 and Jungle Scout charge $100+/month. The guardrail ensures every listing meets a quality bar before publication.                                                                                                                                                     |
| **Skills you'll use** | `output_pydantic` for listing structure, no-code guardrail for SEO quality, `context` passing.                                                                                                                                                                                                  |


---

## 4. Code Review Pipeline

> Structured issue extraction, severity guardrails, codebase memory.


|                       |                                                                                                                                                                                                                                                                                                                            |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads a code file and extracts issues into a `CodeReview` model (issues, severity, line numbers, suggestions). A code guardrail ensures every issue has an associated fix suggestion. **Agent 2** prioritizes issues and estimates effort. **Agent 3** drafts PR comments for the reviewer. |
| **Why it matters**    | Code review tools like SonarQube and CodeClimate automate this. Structured output means you can filter by severity, track issues over time, and integrate with CI/CD pipelines programmatically.                                                                                                                             |
| **Skills you'll use** | `output_pydantic` for issue structure, code guardrail (every issue must have a fix), `memory=True` to learn codebase patterns.                                                                                                                                                     |


---

## 5. Financial Compliance Checker

> Structured policy extraction, mandatory validation guardrails, audit trail with memory.


|                       |                                                                                                                                                                                                                                                                                                                          |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What it does**      | **Agent 1** reads a financial report and extracts key figures into a `ComplianceReport` model. A code guardrail validates all currency amounts have proper formatting and units. **Agent 2** checks figures against regulatory thresholds. **Agent 3** generates a compliance summary for sign-off. |
| **Why it matters**    | RegTech is a $10B+ market. Compliance checking is repetitive, expensive, and error-prone. The guardrail ensures numerical accuracy. Memory creates an audit trail across quarterly checks.                                                                                                                                 |
| **Skills you'll use** | `output_pydantic` for financial data, code guardrail for numerical validation, `memory=True` for audit history.                                                                                                                                                                |


---

## 6. Resume Screening Pipeline

> Structured candidate profiles, scoring guardrails, evidence-based matching.


|                       |                                                                                                                                                                                                                                                                                                                                |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What it does**      | **Agent 1** reads a resume and extracts a `CandidateProfile` (skills, experience_years, education, projects). **Agent 2** scores the candidate against a job description with a guardrail ensuring scores are justified with specific evidence. **Agent 3** drafts a shortlist recommendation for the recruiter. |
| **Why it matters**    | Recruiters spend 23 hours screening resumes for one hire. Lever and Greenhouse are adding AI screening. Structured output lets you sort, filter, and compare candidates programmatically.                                                                                                                                       |
| **Skills you'll use** | `output_pydantic` for candidate structure, code guardrail (scores must cite evidence), `FileReadTool` for resume parsing.                                                                                                                                                              |


---

## 7. Incident Response Playbook Generator

> Structured playbooks, safety guardrails, learning from past incidents.


|                       |                                                                                                                                                                                                                                                                                                                                    |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** reads an alert and extracts a structured `IncidentReport` (type, severity, affected_services). **Agent 2** generates a response playbook with a no-code guardrail: "Every step must include a specific command or action, not just a description." **Agent 3** presents the playbook to the on-call engineer. |
| **Why it matters**    | PagerDuty and Opsgenie serve this market. The guardrail ensures playbooks are actionable, not vague. Memory means the system learns from past incidents — the second Kubernetes outage gets a better playbook than the first.                                                                                                       |
| **Skills you'll use** | `output_pydantic` for incident structure, no-code guardrail for actionability, `memory=True` for incident learning.                                                                                                                                                                      |


---

## 8. Research Paper Summarizer

> Structured extraction, citation guardrails, cross-paper memory.


|                       |                                                                                                                                                                                                                                                                                                                    |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What it does**      | **Agent 1** reads a paper and extracts a `PaperSummary` (title, authors, methodology, key_findings, limitations). A code guardrail ensures at least 3 key findings are extracted. **Agent 2** generates a literature review snippet. **Agent 3** drafts a citation entry for the researcher. |
| **Why it matters**    | PhD students spend weeks on literature reviews. Elicit and Semantic Scholar automate this. Structured output means you can aggregate findings across hundreds of papers into a searchable database.                                                                                           |
| **Skills you'll use** | `output_pydantic` for paper structure, code guardrail (minimum 3 findings), `memory=True` to build knowledge across papers.                                                                                                                                                                  |


---

## 9. Customer Feedback Analyzer

> Structured sentiment extraction, quality guardrails, trend tracking with memory.


|                       |                                                                                                                                                                                                                                                                                                                                            |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **What it does**      | **Agent 1** reads customer feedback and extracts a `FeedbackAnalysis` (sentiment, themes, feature_requests, bug_reports). A guardrail validates every theme has at least one supporting quote. **Agent 2** aggregates themes and trends. **Agent 3** drafts a product brief for the PM to review. |
| **Why it matters**    | Productboard and Dovetail charge $100+/month for this. Structured output means you can track sentiment over time, count feature requests, and prioritize programmatically. The guardrail ensures analysis is evidence-based.                                                                      |
| **Skills you'll use** | `output_pydantic` for feedback structure, code guardrail (themes need supporting quotes), `memory=True` to track trends.                                                                                                                                                                         |


---

## 10. Travel Itinerary Planner

> Structured day-by-day plans, budget guardrails, preference memory.


|                       |                                                                                                                                                                                                                                                                                                                                        |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What it does**      | **Agent 1** researches a destination and outputs a structured `Itinerary` (days, activities, estimated_costs, travel_times). A code guardrail ensures the total budget stays within the user's limit. **Agent 2** optimizes the route for minimum travel time. **Agent 3** presents the final plan for traveler review. |
| **Why it matters**    | Travel planning takes hours. Wanderlog and TripIt are building AI planners. The budget guardrail is a real constraint — if the plan exceeds budget, the agent replans automatically. Memory remembers traveler preferences across trips.                                                                                |
| **Skills you'll use** | `output_pydantic` for itinerary structure, code guardrail (budget validation), `memory=True` for preference learning, `EXASearchTool` for research.                                                                                                                                                                   |


---

> **The pattern**: Every project above uses the same core architecture — **structured output** to get clean data, **guardrails** to ensure quality, and **memory** to get smarter over time. These three features turn a demo into a production-grade system. Pick any project, define your Pydantic models, write your guardrails, and you have a reliable AI pipeline.

