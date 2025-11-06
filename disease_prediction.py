API_KEY = st.secrets["OPENROUTER_API_KEY"]

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

st.write(response.status_code, response.text)
