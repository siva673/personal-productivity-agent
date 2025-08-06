# Import necessary libraries
import streamlit as st
import openai
import os
from dotenv import load_dotenv
import datetime

# Load environment variables from a .env file (useful when running locally)
load_dotenv()

# Initialize the OpenAI client using the API key from secrets or environment
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get today’s date in a readable format like "Wednesday, August 06, 2025"
def today_date():
    return datetime.date.today().strftime("%A, %B %d, %Y")

# Create a full weekly plan prompt for the AI based on the user’s goal
def weekly_prompt(goal):
    return f"""
You are a productivity assistant. The user wants to achieve this goal: "{goal}".

Create a 7-day plan. Each day should include:
- One task
- A motivational quote
- One helpful resource (such as a video, article, or app)

Start the plan from {today_date()}.
Use this format:
Day 1 - [Day Name]
Task: ...
Motivation: ...
Resource: ...
"""

# Create a one-day plan prompt for the AI based on the user’s goal
def daily_prompt(goal):
    return f"""
You are a productivity assistant. The user wants a plan for today to achieve the goal: "{goal}".

Today is {today_date()}.
Provide:
- One task
- A motivational quote
- One useful learning resource
"""

# Send the prompt to OpenAI and get the response
def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",  # You can change the model if needed
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7  # Controls how creative the output is
    )
    return response.choices[0].message.content

# ---------- Streamlit Interface Starts Here ----------

# Set the page title
st.set_page_config(page_title="Productivity Planner")

# App title displayed at the top
st.title("Personal Productivity Plan")

# Text input box for the user to enter their goal
goal = st.text_input("What is your goal? (for example: Learn Python, Get in shape)")

# Two side-by-side buttons: one for weekly, one for daily plan
col1, col2 = st.columns(2)
with col1:
    weekly_button = st.button("Generate 7-Day Plan")
with col2:
    daily_button = st.button("Generate Today's Plan")

# If user clicks weekly button and provided a goal
if weekly_button and goal.strip():
    with st.spinner("Creating your 7-day plan..."):
        result = generate_response(weekly_prompt(goal))
        st.text_area("Your Weekly Plan", value=result, height=400)

# If user clicks daily button and provided a goal
if daily_button and goal.strip():
    with st.spinner("Creating your plan for today..."):
        result = generate_response(daily_prompt(goal))
        st.text_area("Your Plan for Today", value=result, height=300)

# Show warning if user didn’t enter a goal
if (weekly_button or daily_button) and not goal.strip():
    st.warning("Please enter a goal before generating a plan.")
