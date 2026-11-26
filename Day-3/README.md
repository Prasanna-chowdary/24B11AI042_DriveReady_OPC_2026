# Day 3: Building CareerPilot AI with LangChain & Groq

## 🌟 Project Overview

CareerPilot AI is an AI-powered Career and Internship Guidance Assistant developed using Python, LangChain, and Groq LLM.

It helps students explore career opportunities, create learning roadmaps, improve resumes, prepare for technical interviews, and get internship guidance.

---

## 📁 Project Files

- [`Task3.py`](Task3.py) – Main Python script containing the CareerPilot AI chatbot, conversation history, evaluation system, and agent implementation.
- [`careerpilot_test.csv`](careerpilot_test.csv) – Dataset containing test questions and expected keywords to evaluate chatbot responses.

---

## 🧠 Features Implemented

### 1. AI-Powered Career Guidance
- Integrated Groq LLM using `ChatGroq`.
- Used the `openai/gpt-oss-120b` model.
- Created a system prompt to define CareerPilot AI's role and responsibilities.
- Generated guidance for Python learning, career development, and internships.

### 2. Chatbot Memory
- Implemented conversation history using a Python list.
- Stored user questions and AI responses.
- Enabled the chatbot to remember previous conversation details, such as the student's name.

### 3. Automated Response Testing
- Created a CSV-based testing system.
- Implemented the `run_tests()` function.
- Evaluated responses against expected keywords.
- Displayed PASS/FAIL results for each test case.

**Evaluation Summary:**

| Metric | Result |
|---|---|
| Total Test Cases | 5 |
| Passed | 5 |
| Failed | 0 |
| Success Rate | 100% |

### 4. AI Agent Implementation
- Created a basic agent using LangChain's `create_agent()`.
- Connected the agent with the Groq language model.
- Tested the agent with a Python internship preparation query.

---

## ⚙️ Technologies & Libraries

- Python
- LangChain
- LangChain-Groq
- Groq API
- CSV

---

## ▶️ How to Run

### Install Dependencies

```bash
pip install langchain langchain-groq
```

### Configure API Key

Set your Groq API key as the `GROQ_API_KEY` environment variable.

For Google Colab, load it using:

```python
from google.colab import userdata
import os

os.environ["GROQ_API_KEY"] = userdata.get("GROQ_API_KEY")
```

### Execute the Program

```bash
python task.py
```

---

## 🎓 What I Learned

- Building AI-powered applications using LangChain and Groq.
- Connecting prompts, LLMs, and output parsers.
- Maintaining conversation context using chat history.
- Testing LLM responses through CSV-based evaluation.
- Understanding the fundamentals of AI agent creation.

---

**Day 3 Completed – CareerPilot AI | Agentic AI Learning Journey 🚀**
