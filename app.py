import streamlit as st
import random

st.title("🚀 AI Chatbot - Tanush Portfolio")
st.write("Demonstrating AI fundamentals and deployment capabilities")

responses = {
    "hello": "Hello! I'm a web-deployed AI assistant from Tanush's portfolio!",
    "how are you": "Running smoothly on Streamlit - ready for production deployment!",
    "what can you do": "I showcase technical execution skills: Python, web deployment, and AI integration!",
    "tell me about yourself": "I'm part of Tanush's journey to build world-class AI companies. This is step one.",
    "bye": "Thanks for testing! Check out the GitHub repository for the code."
}

random_responses = [
    "Interesting! I'm designed to demonstrate web deployment skills.",
    "As a portfolio project, I'm constantly evolving with new features.",
    "This interface shows the transition from terminal to web applications.",
    "Behind me is Python code ready for AI company infrastructure."
]

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type hello, how are you, etc..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    user_input = prompt.lower().strip()
    if user_input in responses:
        response = responses[user_input]
    else:
        response = random.choice(random_responses)
    
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.rerun()
