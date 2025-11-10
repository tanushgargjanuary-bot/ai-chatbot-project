import streamlit as st
import random
import time

st.title("🚀 AI Chatbot - Tanush Portfolio")
st.write("Now with typing indicators for premium UX")

# Chat responses
responses = {
    "hello": "Hello! I'm a web-deployed AI assistant from Tanush's portfolio!",
    "how are you": "Running smoothly on Streamlit - ready for production deployment!",
    "what can you do": "I showcase technical execution skills: Python, web deployment, and AI integration!",
    "tell me about yourself": "I'm part of Tanush's secret journey, please keep using me once in a while for updates on this application.",
    "bye": "Thanks for testing! Check out the GitHub repository for the code.",
    "what is streamlit": "Streamlit is a Python framework that turns data scripts into shareable web apps in minutes.",
    "show me the code": "Check the GitHub repository: https://github.com/tanushgargianuary-bot/ai-chatbot-project"
}

random_responses = [
    "Interesting! I'm designed to demonstrate web deployment skills.",
    "As a portfolio project, I'm constantly evolving with new features.",
    "This interface shows the transition from terminal to web applications.",
    "Behind me is Python code ready for AI company infrastructure."
]

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Sidebar with prompt suggestions
st.sidebar.markdown("### 💡 Try these prompts:")
for prompt in ["hello", "how are you", "what can you do", "tell me about yourself", "bye"]:
    if st.sidebar.button(prompt):
        st.session_state.messages.append({"role": "user", "content": prompt})

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# NEW: Typing indicator function
def show_typing_indicator():
    with st.chat_message("assistant"):
        with st.empty():
            for i in range(3):
                st.write("🤖 Typing" + "." * (i + 1))
                time.sleep(0.5)

# Handle all messages
if st.session_state.messages:
    last_message = st.session_state.messages[-1]
    if last_message["role"] == "user":
        # Show typing indicator
        show_typing_indicator()
        
        # Generate response
        user_input = last_message["content"].lower().strip()
        if user_input in responses:
            response = responses[user_input]
        else:
            response = random.choice(random_responses)
        
        # Replace typing indicator with actual response
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# Chat input
if prompt := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()
