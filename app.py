import os
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Initialize AI Model
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash-exp", google_api_key=GOOGLE_API_KEY)

# Define a Prompt Template
prompt = PromptTemplate(
    input_variables=["source", "destination"],
    template="""
    Provide the best travel options from {source} to {destination}.
    Include estimated costs for cab, train, bus, and flights.
    Format the response in a structured way.
    """
)

# Streamlit UI
st.title("AI-Powered Travel Planner")
source = st.text_input("Enter Source:")
destination = st.text_input("Enter Destination:")

if st.button("Find Travel Options"):
    if source and destination:
        messages = [
            SystemMessage(content="You are an AI travel assistant. Provide detailed and structured travel recommendations."),
            HumanMessage(content=f"Find the best travel options from {source} to {destination}, including estimated costs for cab, train, bus, and flights.")
        ]
        response = llm(messages)
        st.write("### Travel Recommendations:")
        st.write(response.content)
    else:
        st.warning("Please enter both source and destination.")