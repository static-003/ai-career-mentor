import os
import streamlit as st
from langchain.chat_models import ChatOpenAI

# Get the API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Streamlit app title
st.title("Career Mentor Chatbot")

if not openai_api_key or not openai_api_key.startswith("sk-"):
    st.error("The API key is invalid or not set. Please check your environment variable.")
    st.stop()

# Initialize the ChatOpenAI model
llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)

# Input from the user
user_input = st.text_input("Ask your career-related question:")

# Process the input and generate a response
if user_input:
    try:
        # Pass the input as the 'text' argument
        response = llm.predict(text=user_input)
        st.write("Chatbot Response:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred: {e}")