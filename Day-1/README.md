# Day 1 – Chatbot Development using LangChain and Groq

## Project Overview
This project demonstrates the development of a simple AI-powered chatbot for **Sweet Crumbs Home Bakery** using LangChain and Groq.

The chatbot answers customer queries related to bakery orders while following predefined instructions and business rules.

## Technologies Used
- Python
- LangChain
- Groq API
- Google Colab
- LLM (Large Language Model)

## Features
- Answers customer questions about bakery orders.
- Provides information about order requirements.
- Supports eggless cake availability.
- Follows predefined system instructions.
- Generates polite and concise responses.
- Uses Prompt Guard to demonstrate protection against unsafe prompts.

## Business Rules
1. Orders require at least 24 hours' notice.
2. All cakes have eggless versions.
3. The chatbot should never promise delivery times.
4. If information is unknown, the chatbot should clearly say so.
5. Responses should be polite and under 60 words.

## Implementation
1. Installed and imported LangChain Groq.
2. Configured the Groq API key using Google Colab Secrets.
3. Initialized the language model.
4. Created a system prompt with bakery-specific instructions.
5. Developed an `ask()` function to process customer queries.
6. Tested the chatbot with a sample customer question.
7. Explored Prompt Guard for unsafe prompt detection.

## How to Run
1. Open `Task1.ipynb` in Google Colab.
2. Install the required dependencies.
3. Add your Groq API key to Google Colab Secrets with the name `GROQ_API_KEY`.
4. Run all notebook cells.
5. Enter customer questions using the `ask()` function.

## Sample Query
**Input:**
Can I get my order tomorrow at 9:00 PM?

**Expected Behaviour:**
The chatbot checks the predefined business rules and avoids making unconfirmed delivery-time promises.

## Learning Outcomes
- Understanding LLM integration.
- Working with LangChain and Groq.
- Creating system prompts.
- Handling API keys securely.
- Understanding basic prompt safety concepts.

---
**Day 1 Task – AI Chatbot Development**
