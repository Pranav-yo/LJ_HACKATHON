import streamlit as st
import json
import google.generativeai as genai

# --------------------------
# Gemini 2.0 Setup
# --------------------------
API_KEY = "AIzaSyArRptPxPbhKUq0b7wkDf0L3uTzuIMBrDE"  # 🔑 Replace with your Gemini API key
genai.configure(api_key=API_KEY)

# Use Gemini 2.0 Flash model
model = genai.GenerativeModel("gemini-2.0-flash")

# --------------------------
# Load Financial Data
# --------------------------
with open("finance.json", "r") as f:
    finance_data = json.load(f)

# --------------------------
# Session State
# --------------------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "permissions" not in st.session_state:
    st.session_state.permissions = {
        "assets": True,
        "liabilities": True,
        "transactions": True,
        "epf": True,
        "credit_score": True,
        "investments": True
    }

# --------------------------
# Streamlit Page Config
# --------------------------
st.set_page_config(page_title="AI Finance Assistant", page_icon="💰", layout="wide")

st.title("💬 AI Finance Assistant (Gemini 2.0)")

# --------------------------
# Sidebar - Data Permissions
# --------------------------
with st.sidebar:
    st.header("🔐 Data Permissions")
    for key in st.session_state.permissions.keys():
        st.session_state.permissions[key] = st.checkbox(
            key.capitalize(), value=st.session_state.permissions[key]
        )

# --------------------------
# Chat Display
# --------------------------
chat_container = st.container()
with chat_container:
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

# --------------------------
# Chat Input
# --------------------------
if user_input := st.chat_input("Ask about your money..."):
    # Save user message
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Filter finance data based on active permissions
    filtered_data = {
        k: v for k, v in finance_data.items() if st.session_state.permissions.get(k, False)
    }

    # Prompt for Gemini
    prompt = (
        f"You are a helpful personal finance assistant. "
        f"Use only this financial data: {json.dumps(filtered_data)}.\n"
        f"User: {user_input}"
    )

    try:
        response = model.generate_content(prompt)
        answer = response.text
    except Exception as e:
        answer = f"⚠️ Error: {e}"

    # Save assistant response
    st.session_state.messages.append({"role": "assistant", "content": answer})

    st.rerun()
