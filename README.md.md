# Personal Productivity AI Agent

This is a simple web app I built using Python and Streamlit. The goal is to let anyone enter a personal goal (like “Learn SQL” or “Get in shape”) and get back a personalized 7-day plan.

Each day includes:
- A task
- A motivational quote
- A resource (like a video or article)

The AI behind this is powered by OpenAI’s GPT-4o.

---

## Features

- Web-based, no installation needed (just open in browser)
- Uses GPT-4o to generate custom 7-day plans
- Useful for learning, fitness, career prep, etc.
- Streamlit UI is clean and easy to use

---

## How to Run the App

Make sure you have Python installed.

1. Install the required libraries:
pip install -r requirements.txt
2. Add your oenAI API key in a .env file:
OPENAI_API_KEY=your-openai-key
3.run  app with:
streamlit run productivity_agent_app.py

## Why I built this
I wanted to create a useful AI project that could help people stay on track with their goals. It was also a great way to practice working with APIs, environment variables, and Streamlit for UI.

This is one of the weekly AI projects I’m building and sharing on LinkedIn
Credits
Project by Sivakumar Kolluru
Built with: Python, Streamlit, OpenAI API