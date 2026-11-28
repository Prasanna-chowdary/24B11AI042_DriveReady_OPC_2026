# Day 5 – CareerPilot AI (RAG Chatbot)

## Project Description
CareerPilot AI is a career and internship guidance chatbot designed to help college students with their career-related questions.

It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from an uploaded PDF and generate answers using an LLM.

## Technologies Used
- Python
- LangChain
- Groq API
- Sentence Transformers
- FAISS
- PyMuPDF
- Google Colab

## Features
- Upload career-related PDF documents.
- Extract text from PDF files.
- Split text into smaller chunks.
- Generate embeddings using Sentence Transformers.
- Store embeddings in a FAISS vector database.
- Retrieve the top 3 relevant text chunks.
- Generate answers using the Groq LLM.
- Interactive question-and-answer chatbot.

## Workflow
1. Install the required libraries.
2. Configure the Groq API key using Google Colab Secrets.
3. Upload a PDF document.
4. Extract text from the PDF.
5. Split the extracted text into chunks.
6. Generate embeddings.
7. Store embeddings in FAISS.
8. Retrieve relevant information based on the user's question.
9. Generate and display the answer using Groq.

## How to Run
1. Open the notebook in Google Colab.
2. Add your Groq API key in Colab Secrets with the name `groq_api_key`.
3. Run all the code cells.
4. Upload a career-related PDF when prompted.
5. Ask career-related questions in the chatbot.

## Model Used
`openai/gpt-oss-120b`

## Embedding Model
`all-MiniLM-L6-v2`

## Project Name
**CareerPilot AI – Career & Internship Guidance Assistant**
