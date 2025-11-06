import os
import pickle
import requests
import streamlit as st
from streamlit_option_menu import option_menu

# ✅ Always keep secret loading AFTER import streamlit
API_KEY = st.secrets.get("OPENROUTER_API_KEY")

if not API_KEY:
    st.error("❌ OPENROUTER_API_KEY not found. Add it in Streamlit → Settings → Secrets.")
    st.stop()

url = "https://openrouter.ai/api/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    # "HTTP-Referer": "https://edunet-foundation-tech-saksham-project-zkc8v9rjayuy9zhjjzcslv.streamlit.app/",
    "X-Title": "Dr A.D.K Health Assistant"
}

data = {
    "model": "deepseek/deepseek-r1",
    "messages": [
        {"role": "system", "content": "You are a helpful medical assistant."},
        {"role": "user", "content": "Hello doctor, what should a diabetic person eat?"}
    ]
}

response = requests.post(url, headers=headers, json=data)

# ✅ print what actually happens (for debugging)
st.write("Status code:", response.status_code)
st.code(response.text)
