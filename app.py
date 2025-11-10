import streamlit as st
import random

# ===== APP CONFIGURATION =====
st.title("🚀 AI Chatbot - Tanush Portfolio")
st.write("Demonstrating AI fundamentals and deployment capabilities")

# ===== CHATBOT BRAIN =====
# Dictionary of known questions and answers
responses = {
    "hello": "Hello! I'm a web-deployed AI assistant from Tanush's portfolio!",
    "how are you": "Running smoothly on Streamlit - ready for production deployment!",
    "what can you do": "I showcase technical execution skills: Python, web deployment, and AI integration!",
    "tell me about yourself": "I'm part of Tanush's secret journey, please keep using me once in a while for updates on this application.",
    "bye": "Thanks for testing! Check out the GitHub repository for the code."
}

# Random answers for unknown questions
random_responses = [
    "Interesting! I'm designed to demonstrate web deployment skills.",
    "As a portfolio project, I'm constantly evolving with new features.",
    "This interface shows the transition from terminal to web applications.",
    "Behind me is Python code ready for AI company infrastructure."
]

# ===== MEMORY SYSTEM =====
# Creates chat history that persists during the session
if "messages" not in st.session_state:
    st.session_state.messages = []

# ===== SIDEBAR WITH PROMPT SUGGESTIONS =====
st.sidebar.markdown("### 💡 Try these prompts:")
suggested_prompts = ["hello", "how are you", "what can you do", "tell me about yourself", "bye"]

# Create clickable prompt buttons
for prompt in suggested_prompts:
    if st.sidebar.button(prompt):
        # Simulate user typing this prompt
        st.session_state.messages.append({"role": "user", "content": prompt})
        # Generate bot response
        user_input = prompt.lower().strip()
        if user_input in responses:
            response = responses[user_input]
        else:
            response = random.choice(random_responses)
        st.session_state.messages.append({"role": "assistant", "content": response})

# ===== DISPLAY CHAT HISTORY =====
# Show all previous messages in the chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ===== CHAT INPUT =====
# Main text box at bottom for user typing
if prompt := st.chat_input("Type a message or use sidebar prompts..."):
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Generate bot response
    user_input = prompt.lower().strip()
    if user_input in responses:
        response = responses[user_input]
    else:
        response = random.choice(random_responses)
    
    # Add bot response to history
    st.session_state.messages.append({"role": "assistant", "content": response})
    
    # Refresh to show new messages
    st.rerun()
