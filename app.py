import streamlit as st
import random
import time
import numpy as np

# Your trained color AI model
color_words = ["red", "green", "blue", "yellow", "purple", "orange", 
               "pink", "brown", "black", "white", "gold", "silver"]
color_weights = np.array([
    [ 1.0, -0.0,  0.0],  # red
    [-0.0,  1.0, -0.0],  # green
    [ 0.0,  0.0,  1.0],  # blue
    [ 1.0,  1.0,  0.0],  # yellow
    [ 0.5,  0.0,  0.5],  # purple
    [ 1.0,  0.5,  0.0],  # orange
    [ 1.0,  0.75, 0.8],  # pink
    [ 0.6,  0.3,  0.0],  # brown
    [ 0.0,  0.0,  0.0],  # black
    [ 1.0,  1.0,  1.0],  # white
    [ 1.0,  0.84, 0.0],  # gold
    [ 0.75, 0.75, 0.75]  # silver
])

def predict_color(word):
    """Use your trained AI to predict RGB values for color words"""
    if word in color_words:
        idx = color_words.index(word)
        rgb_values = color_weights[idx]
        return rgb_values
    return None

st.title("🚀 AI Chatbot - Tanush Portfolio")
st.write("Now with AI Color Understanding!")

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

# FIXED: Simple typing indicator without time.sleep()
def show_typing_indicator():
    with st.chat_message("assistant"):
        st.markdown("🤖 Thinking...")

# Handle all messages
if st.session_state.messages:
    last_message = st.session_state.messages[-1]
    if last_message["role"] == "user":
        # Show typing indicator
        show_typing_indicator()
        
        # Generate response
        user_input = last_message["content"].lower().strip()

        # First, check if user is asking about colors
        color_response = None
        for color_word in color_words:
            if color_word in user_input:
                rgb = predict_color(color_word)
                if rgb is not None:
                    color_response = f"🎨 The color '{color_word}' is RGB: [{rgb[0]:.2f}, {rgb[1]:.2f}, {rgb[2]:.2f}]"
                    break

        # Choose response source based on content
        if color_response:
            response = color_response  # Use AI color prediction
        elif user_input in responses:
            response = responses[user_input]  # Use existing scripted responses
        else:
            response = random.choice(random_responses)  # Fallback to random
        
        # Replace typing indicator with actual response
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()

# Chat input
if prompt := st.chat_input("Type a message..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.rerun()
