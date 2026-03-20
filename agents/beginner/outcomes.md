# What Can You Build Now?

You've just learned the fundamentals of CrewAI — defining an **Agent** with a role, goal, and backstory, writing a **Task** with structured instructions and input placeholders, wiring them into a **Crew**, and running it all with `kickoff()`. These are the same building blocks behind every AI agent system in production today.

Here are **10 real-world projects** you can build right now with what you've learned.

---

## 1. Resume Screener

> Instantly evaluate whether a candidate is a fit for a role.

| | |
|---|---|
| **What it does** | Takes a job description and resume text as input. The agent evaluates the resume against the JD and returns a fit verdict — `Strong Fit`, `Moderate Fit`, or `Weak Fit` — with a short justification. |
| **Why it matters** | Recruiters spend ~7 seconds scanning a resume. This agent does it in under 3 seconds with consistent criteria every time. Companies like HireVue and Lever use similar AI screening at scale. |
| **Skills you'll use** | Single agent, dual-input placeholders (`{resume}`, `{job_description}`), structured classification output. |

---

## 2. Product Review Sentiment Analyzer

> Turn thousands of customer reviews into actionable sentiment data.

| | |
|---|---|
| **What it does** | Takes a product review and classifies it as `Positive`, `Negative`, or `Neutral` with a one-line explanation of the primary sentiment driver. |
| **Why it matters** | E-commerce brands like Amazon and Shopify merchants process millions of reviews. Automated sentiment analysis powers product ranking, seller feedback, and trend detection. |
| **Skills you'll use** | Single agent, text classification with reasoning, structured expected output. |

---

## 3. Email Tone Rewriter

> Rewrite any email to match the exact tone you need.

| | |
|---|---|
| **What it does** | Takes a draft email and a desired tone (`formal`, `friendly`, `apologetic`, `urgent`) and rewrites the email while preserving the original meaning. |
| **Why it matters** | Tone mismatches cause real business damage — a blunt email to a client, or an overly casual message to a VP. Tools like Grammarly's tone detector are built on this exact pattern. |
| **Skills you'll use** | Single agent, dual-input placeholders (`{email}`, `{tone}`), text transformation task. |

---

## 4. Meeting Notes Summarizer

> Turn a raw meeting transcript into structured, actionable notes.

| | |
|---|---|
| **What it does** | Takes a meeting transcript and produces a structured summary: key decisions made, action items with owners, deadlines mentioned, and open questions. |
| **Why it matters** | Otter.ai, Fireflies.ai, and Notion AI all monetize meeting summarization. Every company with remote teams needs this — it's one of the highest-demand AI use cases in the enterprise. |
| **Skills you'll use** | Single agent, long-form input via `{transcript}` placeholder, structured multi-section expected output. |

---

## 5. Cold Outreach Email Generator

> Generate personalized sales emails that don't sound like templates.

| | |
|---|---|
| **What it does** | Takes a target company name and your product description, then generates a personalized cold outreach email with a compelling subject line, pain-point hook, and clear CTA. |
| **Why it matters** | Sales teams at companies like Outreach.io and Apollo.io use AI-generated personalized emails to increase reply rates by 2-3x over generic templates. |
| **Skills you'll use** | Single agent, dual-input placeholders (`{company}`, `{product}`), content generation task. |

---

## 6. Code Explainer

> Make any code snippet understandable to a non-technical audience.

| | |
|---|---|
| **What it does** | Takes a code snippet and explains it in plain English — what it does, how it works step by step, and what the output would be. |
| **Why it matters** | Developer documentation tools like Mintlify and ReadMe use AI code explanation to auto-generate docs. It's also the core feature behind GitHub Copilot's "Explain this code" button. |
| **Skills you'll use** | Single agent, `{code}` input placeholder, step-by-step analytical output — mirrors the code reviewer example from the workshop. |

---

## 7. Social Media Caption Generator

> Create platform-specific captions from a single product description.

| | |
|---|---|
| **What it does** | Takes a product or event description and a target platform (`Twitter`, `LinkedIn`, `Instagram`), then generates an optimized caption with appropriate tone, length, hashtags, and formatting. |
| **Why it matters** | Social media managers handle 5-10 platforms daily. Tools like Hootsuite and Buffer have integrated AI caption generation as a core feature because it saves hours per week. |
| **Skills you'll use** | Single agent, dual-input placeholders (`{description}`, `{platform}`), platform-aware content generation. |

---

## 8. Legal Clause Simplifier

> Translate legalese into plain English anyone can understand.

| | |
|---|---|
| **What it does** | Takes a legal clause or contract paragraph and rewrites it in clear, simple language while preserving the legal meaning. Flags any potentially risky terms. |
| **Why it matters** | Legal tech is a $28B market. Tools like DoNotPay and Juro use AI to simplify contracts for non-lawyers. Most people sign agreements they don't fully understand — this agent fixes that. |
| **Skills you'll use** | Single agent, `{clause}` input placeholder, text transformation with domain-specific constraints. |

---

## 9. Interview Question Generator

> Generate tailored interview questions for any role and level.

| | |
|---|---|
| **What it does** | Takes a job role and seniority level (`junior`, `mid`, `senior`, `lead`) and generates 10 targeted interview questions — a mix of technical, behavioral, and situational — with brief notes on what a good answer looks like. |
| **Why it matters** | HR platforms like Greenhouse and Lever are adding AI interview prep. Engineering managers spend 30+ minutes writing questions per candidate — this agent does it in seconds. |
| **Skills you'll use** | Single agent, dual-input placeholders (`{role}`, `{level}`), structured list output with sub-items. |

---

## 10. Startup Idea Validator

> Get a quick, structured reality check on any startup idea.

| | |
|---|---|
| **What it does** | Takes a startup idea description and returns a structured analysis: target market size, competitive landscape, key risks, feasibility score (1-10), and a one-line verdict (`Pursue` / `Pivot` / `Pass`). |
| **Why it matters** | YC and other accelerators evaluate thousands of ideas per batch. Founders use structured frameworks like Lean Canvas to validate ideas — this agent automates that first-pass analysis. |
| **Skills you'll use** | Single agent, `{idea}` input placeholder, multi-section analytical output with scoring. |

---

> **Tip**: Each of these projects follows the same pattern you learned in the workshop — define an Agent, write a Task, create a Crew, and `kickoff()`. The only things that change are the role, the instructions, and the input placeholders. Start with one, get it working, then try another.
