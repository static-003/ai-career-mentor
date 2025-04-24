import os
import streamlit as st
from langchain.chat_models import ChatOpenAI

# Streamlit app title
st.title("Career Mentor Chatbot")

# Get the API key from environment variables
openai_api_key = os.getenv("OPENAI_API_KEY")

# Check if the API key is valid
if not openai_api_key or not openai_api_key.startswith("sk-"):
    st.error("The API key is invalid or not set. Please check your environment variable.")
    st.stop()

# Initialize the ChatOpenAI model
try:
    llm = ChatOpenAI(temperature=0.7, openai_api_key=openai_api_key)
except Exception as e:
    st.error(f"Failed to initialize the ChatOpenAI model: {e}")
    st.stop()

# Input from the user
st.write("Welcome! Ask any career-related question, and I'll do my best to assist you.")
user_input = st.text_input("Enter your question below:")

# Process the input and generate a response
if user_input:
    try:
        # Generate a response using the ChatOpenAI model
        response = llm.predict(text=user_input)
        st.write("### Chatbot Response:")
        st.write(response)
    except Exception as e:
        st.error(f"An error occurred while processing your request: {e}")

# Footer
st.write("---")
st.write("Powered by OpenAI and LangChain")