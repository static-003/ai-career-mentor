import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
import os

os.environ["OPENAI_API_KEY"] = "your-openai-api-key-here"

st.set_page_config(page_title="AI Career Mentor", page_icon="🎓")
st.title("🎓 AI Career Mentor Chatbot")
st.write("Ask me anything about careers, job roles, skills, and learning paths!")

llm = ChatOpenAI(temperature=0.7)
memory = ConversationBufferMemory()
conversation = ConversationChain(llm=llm, memory=memory, verbose=False)

user_input = st.text_input("👤 You:", placeholder="What career suits me if I love math and tech?")

if user_input:
    with st.spinner("Thinking..."):
        response = conversation.predict(input=user_input)
    st.markdown(f"**🤖 AI Mentor:** {response}")

if st.checkbox("Show chat history"):
    st.markdown("### 💬 Previous Conversation")
    for i, msg in enumerate(memory.chat_memory.messages):
        if i % 2 == 0:
            st.markdown(f"**You:** {msg.content}")
        else:
            st.markdown(f"**AI:** {msg.content}")
