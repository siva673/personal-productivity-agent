# Import required libraries
import streamlit as st
import openai
import os
from dotenv import load_dotenv
import datetime

# Load environment variables (useful for local dev)
load_dotenv()

# Initialize the OpenAI client using new SDK structure
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Get today’s date in readable format like "Wednesday, August 06, 2025"
def today_date():
    return datetime.date.today().strftime("%A, %B %d, %Y")

# Prompt for weekly plan
def weekly_prompt(goal):
    return f"""
You are a productivity assistant. The user wants to achieve this goal: "{goal}".

Create a 7-day plan. Each day should include:
- One task
- A motivational quote
- One helpful resource (video, article, or app)

Start the plan from {today_date()}.
Use this format:
Day 1 - [Day Name]
Task: ...
Motivation: ...
Resource: ...
"""

# Prompt for today's plan
def daily_prompt(goal):
    return f"""
You are a productivity assistant. The user wants a plan for today to achieve the goal: "{goal}".

Today is {today_date()}.
Please provide:
- One task
- A motivational quote
- One useful learning resource
"""

# Function to generate response using OpenAI
def generate_response(prompt):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )
    return response.choices[0].message.content

# ---------- Streamlit App UI ----------

st.set_page_config(page_title="Productivity Planner")
st.title("Personal Productivity Plan")

# Input: User's goal
goal = st.text_input("What is your goal? (for example: Learn Python, Get in shape)")

# Buttons for weekly or daily plan
col1, col2 = st.columns(2)
with col1:
    weekly_button = st.button("Generate 7-Day Plan")
with col2:
    daily_button = st.button("Generate Today's Plan")

# Show result if input is valid
if weekly_button and goal.strip():
    with st.spinner("Creating your 7-day plan..."):
        result = generate_response(weekly_prompt(goal))
        st.text_area("Your Weekly Plan", value=result, height=400)

if daily_button and goal.strip():
    with st.spinner("Creating your plan for today..."):
        result = generate_response(daily_prompt(goal))
        st.text_area("Your Plan for Today", value=result, height=300)

# Warn if input is empty
if (weekly_button or daily_button) and not goal.strip():
    st.warning("Please enter a goal before generating a plan.")
