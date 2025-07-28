# 🧠 Job Posting Creator (CrewAI Multi-Agent Project)

This project demonstrates a practical implementation of a multi-agent AI system using the CrewAI framework. It automates the process of generating professional job postings based on a given job title, industry, and location.

## 🔍 Objective

The goal is to simulate how AI agents can collaboratively research, write, and refine a job post—delivering a high-quality, human-like final output. This serves as a beginner-friendly showcase of how to orchestrate structured LLM-powered agents using real-world workflows.

## ⚙️ Project Structure

- **Language Model:** Meta-Llama 3.1 8B via Hugging Face
- **Search Tool:** Serper API for live data search
- **Framework:** CrewAI using YAML-based agent/task configuration

## 🛠️ How It Works

1. **Input:** The user provides three fields — `job_title`, `industry`, and `location`.
2. **Agents:** The system contains three collaborative agents:
   - `Job Researcher`: Gathers role-related details via web search.
   - `Job Writer`: Crafts a structured and rich job post based on research.
   - `HR Reviewer`: Edits and refines the post to ensure professional tone and formatting.
3. **Output:** The final job description is generated and saved as a Markdown file (`output/job_posting.md`).

## 🧩 Files Overview

- `main.py` → Runs the workflow and kicks off the crew with your inputs.
- `crew.py` → Defines the crew, agents, tasks, and how they collaborate.
- `agents.yaml` → Agent configurations including role, goal, and backstory.
- `tasks.yaml` → Task descriptions, expected outputs, and agent mappings.
- `.env` → Stores model name and API keys.
- `pyproject.toml` → CrewAI project configuration.
- `job_posting.md` → The generated job post output.

