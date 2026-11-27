# CareerPilot AI – Career & Internship Guidance Assistant

## Project Overview
CareerPilot AI is an AI-powered career and internship guidance assistant designed to help college students make better career decisions and prepare for job opportunities.

It provides personalized guidance based on students' interests, skill levels, and career goals.

## Features
- **Career Guidance:** Suggests suitable career paths based on student interests.
- **Skill Guidance:** Provides beginner-friendly learning roadmaps.
- **Internship Guidance:** Explains how to prepare and apply for internships.
- **Resume Guidance:** Suggests improvements to student resumes.
- **Interview Preparation:** Provides interview topics and preparation tips.
- **Complaint Management:** Collects student complaints and stores them in Google Sheets.

## Technologies Used
- Python
- LangChain
- Groq API
- Google Colab
- Google Sheets
- Pydantic

## AI Model
`openai/gpt-oss-20b` using Groq API.

## Project Structure
The notebook contains four main code cells:

1. **Setup and Authentication**
   - Install required libraries.
   - Connect to Groq API.
   - Authenticate Google account.
   - Create or open a Google Sheet.

2. **Data Models**
   - Define career information.
   - Create a student complaint data model using Pydantic.

3. **AI Tools**
   - Career guidance
   - Skill guidance
   - Internship guidance
   - Resume guidance
   - Interview guidance
   - Student complaint logging

4. **AI Agent**
   - Define the agent instructions.
   - Create the CareerPilot AI agent.
   - Maintain conversation history.
   - Interact with the agent using the chat function.

## How to Run
1. Open the notebook in Google Colab.
2. Add your Groq API key to Colab Secrets with the name `GROQ_API_KEY`.
3. Enable notebook access to the secret.
4. Run the cells in order, from Cell 1 to Cell 4.
5. Authenticate your Google account when prompted.
6. Start interacting with CareerPilot AI.

## Example Questions
- Which career paths can I explore as an AIML student?
- What skills should I learn to become an AI Engineer?
- How can I prepare for internships?
- How can I improve my resume?
- Give me interview preparation tips for a Python developer.

## Future Enhancements
- Add real-time internship search.
- Provide personalized career recommendations.
- Add resume upload and analysis.
- Develop a simple web-based chatbot interface.

