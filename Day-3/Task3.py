"""
Day 3: LangChain LCEL, Evaluation Harness and Agent Foundations
Project: CareerPilot AI - Career & Internship Guidance Assistant

Install:
    pip install -U langchain langchain-groq

"""

import os
import csv
from pathlib import Path

from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain.agents import create_agent


# 1. Connect to the Groq model
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError(
        "GROQ_API_KEY is missing. Set your Groq API key as an environment variable."
    )

llm = ChatGroq(
    model="openai/gpt-oss-120b",
    temperature=0.3
)


# 2. Define the CareerPilot AI assistant's role and rules
SYSTEM = """
ROLE:
You are CareerPilot AI, a friendly career and internship guidance assistant
for college students, especially beginners.

YOU CAN HELP WITH:
- Choosing suitable career paths based on a student's interests and skills.
- Suggesting technical skills and learning roadmaps.
- Giving internship preparation guidance.
- Improving resume content and project descriptions.
- Preparing students for technical interviews.

RULES:
- Give simple, practical, step-by-step explanations.
- Ask a relevant follow-up question when important information is missing.
- Do not guarantee jobs, internships, selections, or salaries.
- Do not invent current job or internship openings.
- If you do not know a current opportunity's details, say that the student
  should verify it on the company's official website.
- Encourage students to build projects and practise consistently.

FORMAT:
Be friendly, supportive, and concise. Reply in English or Telugu according
to the student's language.
"""


# 3. Create an LCEL prompt and chain
prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

chain = prompt | llm | StrOutputParser()


# 4. Store conversation history
history = []

def ask(question: str) -> str:
    """Send a question to CareerPilot AI and remember the conversation."""
    answer = chain.invoke({
        "history": history,
        "question": question
    })

    history.extend([
        ("human", question),
        ("ai", answer)
    ])

    return answer


# 5. Test conversational memory
def demo_chat() -> None:
    print("\n--- CareerPilot AI: Conversation Demo ---")

    print("Student:", "Hi, my name is Ravi. I am interested in Python.")
    print("CareerPilot:", ask(
        "Hi, my name is Ravi. I am interested in Python."
    ))

    print("\nStudent:", "What is my name?")
    print("CareerPilot:", ask("What is my name?"))


# 6. Evaluate the assistant using the provided CSV test cases
def run_tests(path: str = "careerpilot_test.csv") -> None:
    """Check whether answers contain the expected keyword from the CSV."""
    csv_path = Path(__file__).resolve().parent / path

    if not csv_path.exists():
        print(f"\nTest file not found: {csv_path}")
        print("Keep careerpilot_test.csv in the same folder as task.py.")
        return

    with csv_path.open("r", encoding="utf-8", newline="") as file:
        rows = list(csv.DictReader(file))

    if not rows:
        print("\nNo test cases found in the CSV file.")
        return

    passed = 0
    print("\n--- CareerPilot AI: Evaluation Results ---")

    for row in rows:
        question = row["question"]
        expected = row["must_include"]

        # Use a fresh conversation for every test
        answer = chain.invoke({
            "history": [],
            "question": question
        })

        success = expected.lower() in answer.lower()

        if success:
            passed += 1

        print(
            ("PASS" if success else "FAIL"),
            "|",
            question,
            "->",
            answer[:120].replace("\n", " ")
        )

    percentage = (passed / len(rows)) * 100
    print(f"\n{passed}/{len(rows)} tests passed ({percentage:.0f}%).")


# 7. Create a basic agent (tools can be added in a later task)
def agent_demo() -> None:
    print("\n--- CareerPilot AI: Agent Foundation ---")

    agent = create_agent(
        model=llm,
        tools=[],
        system_prompt=SYSTEM
    )

    result = agent.invoke({
        "messages": [
            {
                "role": "user",
                "content": "Give me three beginner-friendly steps to prepare for a Python internship."
            }
        ]
    })

    print(result["messages"][-1].content)


if __name__ == "__main__":
    demo_chat()
    run_tests()
    agent_demo()
